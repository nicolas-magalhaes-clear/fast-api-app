from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_async_db
from app.services.products_service import ProductsService
from app.schemas.products_schemas import ProductOut, ProductCreate
from app.dependencies.auth import get_current_user_dependency
from typing import List, Dict, Any

products_router = APIRouter()

@products_router.get("/", response_model=List[ProductOut])
async def index(
    db: AsyncSession = Depends(get_async_db),
    current_user: Dict[str, Any] = Depends(get_current_user_dependency)
):
    service = ProductsService(db)
    products = await service.get_all()
    return [ProductOut.model_validate(product) for product in products]

@products_router.get('/{product_id}')
async def show(
    product_id: int,
    db: AsyncSession = Depends(get_async_db),
    current_user: Dict[str, Any] = Depends(get_current_user_dependency)
):
    service = ProductsService(db)
    return await service.get_one_by_id(product_id)

@products_router.post("/", response_model=ProductOut)
async def create(
    product: ProductCreate,
    db: AsyncSession = Depends(get_async_db),
    current_user: Dict[str, Any] = Depends(get_current_user_dependency)
):
    service = ProductsService(db)
    created_product = await service.create(product)
    await db.refresh(created_product, ['categories'])
    return ProductOut.model_validate(created_product)