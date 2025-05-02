from fastapi import APIRouter, Depends
from app.db.session import get_async_db
from app.schemas.auth_schemas import LoginPayload, SignupPayload
from app.schemas.users_schemas import UserResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.auth_service import AuthService
from fastapi.responses import JSONResponse

auth_router = APIRouter()



@auth_router.post("/login", tags=["auth"], response_model=UserResponse)
async def login(user_data : LoginPayload, db : AsyncSession = Depends(get_async_db)):
    auth_service = AuthService(db)
    data =  await auth_service.login(user_data.email, user_data.password)

    return JSONResponse(
        status_code=200,
        content={
            **UserResponse.model_validate(data["user"]).model_dump()
        },
        headers={
            "Authorization": str(data["authorization"])
        }
    )
  
@auth_router.post("/signup", tags=["auth"], response_model=UserResponse)
async def signup(signup_data : SignupPayload, db : AsyncSession = Depends(get_async_db)):
    auth_service = AuthService(db)
    data = await auth_service.signup(SignupPayload(
      email=signup_data.email,
      password=signup_data.password
    ))
    return JSONResponse(
      status_code=200,
      content={
        **UserResponse.model_validate(data["user"]).model_dump()
      },
      headers={
        "Authorization": str(data["authorization"])
      }
    )
  
  