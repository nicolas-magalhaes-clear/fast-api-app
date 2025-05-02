from app.models.user import User
import jwt
from datetime import datetime, timedelta
from typing import Optional

SECRET_KEY : str = "seu_segredo_aqui"
ALGORITHM = "HS256"

def create_access_token(user : User, expires_delta: Optional[timedelta] = None):
  expire = None
  to_encode = user.to_dict()
  if expires_delta:
    expire = datetime.now() + expires_delta
  else:
    expire = datetime.now() + timedelta(hours=24)
  to_encode.update({'exp': expire})
  encoded_jwt = jwt.encode(to_encode, str(SECRET_KEY), algorithm=ALGORITHM)
  return encoded_jwt
