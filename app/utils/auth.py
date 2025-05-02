from jwt import encode, ExpiredSignatureError, PyJWTError, decode # type: ignore
from datetime import datetime, timedelta
from typing import Any, Dict, Optional
from app.config.constants import constants

ALGORITHM = "HS256"

def create_access_token(user_id : int, expires_delta: Optional[timedelta] = None):
    expire = datetime.now() + (expires_delta or timedelta(hours=24))
    to_encode : Dict[str, Any] = {
        "id": user_id,
        "exp": expire
    }
    encoded_jwt = encode(to_encode, constants.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = decode(token, constants.SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except ExpiredSignatureError:
        raise Exception("Token expired")
    except PyJWTError:
        raise Exception("Token invalid")