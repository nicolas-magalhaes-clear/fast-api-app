from typing import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.category import Category

class CategoriesService:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_by_ids(self, category_ids: list[int]) -> Sequence[Category]:
        result = await self.db.execute(select(Category).where(Category.id.in_(category_ids)))
        return result.scalars().all() 