from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.product import Product
from app.schemas.products_schemas import ProductCreate

class ProductsService:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create(self, data: ProductCreate) -> Product:
        product = Product(**data.model_dump())
        self.db.add(product)
        await self.db.commit()
        await self.db.refresh(product)
        return product

    async def get_all(self) -> Sequence[Product]:
        result = await self.db.execute(select(Product))
        return result.scalars().all()
    
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