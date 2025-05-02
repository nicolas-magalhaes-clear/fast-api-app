from sqlalchemy.ext.asyncio import AsyncSession

from app.exceptions.exceptions_types.unauthorized_exception import UnauthorizedException
from app.services import UserService

class AuthService:
  def __init__(self, db  : AsyncSession):
    self.db = db
    self.users_service = UserService(db)
    
  async def login(self, email: str, password: str):
    user = await self.users_service.get_by_email(email)
    if not user or not user.check_password(password):
      raise UnauthorizedException("Password or email is incorrect")
    
    return user