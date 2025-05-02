from pydantic import BaseModel, EmailStr

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    
    class Config:
        orm_mode = True
        
class UserCreatePayload(BaseModel):
    email: EmailStr
    password: str
    
    class Config:
        orm_mode = True