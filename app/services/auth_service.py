from sqlalchemy.ext.asyncio import AsyncSession
from bcrypt import checkpw
from app.exceptions.exceptions_types.unauthorized_exception import UnauthorizedException
from app.schemas.auth_schemas import SignupPayload
from app.schemas.users_schemas import UserCreatePayload
from app.services import UserService
from bcrypt import gensalt, hashpw
from app.utils.auth import create_access_token

class AuthService:
  def __init__(self, db  : AsyncSession):
    self.db = db
    self.users_service = UserService(db)
    
  async def login(self, email: str, password: str) -> dict[str, object]:
    user = await self.users_service.get_by_email(email)
    if not user or not self._compare_password(password, user.password):
      raise UnauthorizedException("Password or email is incorrect")
    authorization = create_access_token(user.id)
    
    return {
    "user": user,  # Assuming 'user' is an object or a dictionary
    "authorization": authorization  # Assuming 'authorization' is a string or token
    }

  
  async def signup(self, signup_data : SignupPayload) -> dict[str, object]:
    user = await self.users_service.get_by_email(signup_data.email)
    if user:
      raise UnauthorizedException("User already exists")
    
    hashed_password = self._hash_password(signup_data.password)
    
    new_user_data = UserCreatePayload(
      email=signup_data.email,
      password=hashed_password,
    )
    new_user = await self.users_service.create(new_user_data)
    authorization = create_access_token(new_user.id)
    
    return {
      "user": new_user,
      "authorization": authorization
    }
  
  
  def _compare_password(self, password: str, hashed_password: str):
      return checkpw(password.encode(), hashed_password.encode())
    
  def _hash_password(self, password: str):
      salt = gensalt()
      return hashpw(password.encode(), salt).decode()