from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.db.session import get_async_db
from ..services.users_service import UserService
from ..schemas.users_schemas import UserResponse

def get_user_service(db: AsyncSession = Depends(get_async_db)):
    return UserService(db)

users_router = APIRouter(tags=["users"])

@users_router.get("/", response_model=List[UserResponse])
async def list_users(
    service: UserService = Depends(get_user_service)
):
    return await service.list_all()

@users_router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    user = await service.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user