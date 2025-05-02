from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_async_db
from app.services.products_service import ProductsService

products_router = APIRouter()

@products_router.get("/")
async def index(db: AsyncSession = Depends(get_async_db)):
    service = ProductsService(db)
    return await service.get_all()

@products_router.get('{product_id}')
async def show(product_id: int, db: AsyncSession = Depends(get_async_db)):
    service = ProductsService(db)
    return await service.get_one_by_id(product_id)