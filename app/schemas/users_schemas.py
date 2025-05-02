from pydantic import BaseModel, EmailStr

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    
    model_config = {
      'from_attributes': True
    }
        
class UserCreatePayload(BaseModel):
    email: EmailStr
    password: str
    
    model_config = {
      'from_attributes': True
    }