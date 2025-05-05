from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from app.models.product import Product
from app.schemas.products_schemas import ProductCreate
from app.services.categories_service import CategoriesService

class ProductsService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.categories_service = CategoriesService(db)
    
    async def create(self, data: ProductCreate) -> Product:
        # Extract category_ids from the data
        category_ids = data.category_ids
        data_dict = data.model_dump()
        data_dict.pop('category_ids', None)
        
        # Create the product
        product = Product(**data_dict)
        
        # If category_ids are provided, fetch and set the categories
        if category_ids:
            categories = await self.categories_service.get_by_ids(category_ids)
            product.categories = list(categories)
        
        self.db.add(product)
        await self.db.commit()
        await self.db.refresh(product)
        
        # Load the categories relationship
        await self.db.refresh(product, ['categories'])
        return product

    async def get_all(self) -> Sequence[Product]:
        result = await self.db.execute(
            select(Product).options(joinedload(Product.categories))
        )
        return result.unique().scalars().all()
    
    async def get_one_by_id(self, product_id: int) -> Product:
        result = await self.db.execute(select(Product).where(Product.id == product_id))
        return result.scalars().first()
    
    async def update(self, product_id: int, data: ProductCreate) -> Product | None:
        product = await self.get_one_by_id(product_id)
        if not product:
            return None
        for key, value in data.model_dump().items():
            setattr(product, key, value)
        await self.db.commit()
        await self.db.refresh(product)
        return product
    
    async def destroy(self, product_id: int) -> None:
        product = await self.get_one_by_id(product_id)
        if not product:
            return None
        await self.db.delete(product)
        await self.db.commit()
        return None