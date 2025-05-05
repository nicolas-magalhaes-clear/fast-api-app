from fastapi import Depends
from app.middleware.auth_middleware import get_current_user
from typing import Dict, Any, Annotated

async def get_current_user_dependency(current_user: Annotated[Dict[str, Any], Depends(get_current_user)]) -> Dict[str, Any]:
    return current_user