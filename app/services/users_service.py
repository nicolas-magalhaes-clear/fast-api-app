from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.users_schemas import UserCreatePayload
from ..models.user import User


class UserService:
  
  def __init__(self, db: AsyncSession ):
    self.db = db
    
  async def list_all(self):
    statement = select(User)
    result = await self.db.execute(statement)
    return result.scalars().all()
  
  async def get_by_email(self, email : str):
    stmt = select(User).where(User.email == email)
    result = await self.db.execute(stmt)
    return result.scalars().first()
  
  async def get_one_by_id(self, id : int):
    statement = select(User).where(User.id == id)
    result = await self.db.execute(statement)
    return result.scalars().first()
  
  async def create(self, user: UserCreatePayload):
    user = User(**user.model_dump())
    self.db.add(user)
    await self.db.commit()
    await self.db.refresh(user) 
    return user
  
  async def destroy(self, id: int):
    user = await self.get_one_by_id(id)
    if not user:
      return None
    await self.db.delete(user)
    await self.db.commit()
    return None
  
