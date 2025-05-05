from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.utils.auth import verify_token
from typing import Optional, Dict, Any

security = HTTPBearer()

async def get_current_user(request: Request) -> Dict[str, Any]:
    try:
        auth_header: Optional[HTTPAuthorizationCredentials] = await security(request)
        if not auth_header:
            raise HTTPException(status_code=401, detail="Not authenticated")
            
        token = auth_header.credentials
        payload = verify_token(token)
        return payload
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e)) 