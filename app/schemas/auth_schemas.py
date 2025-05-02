from pydantic import BaseModel, EmailStr

class LoginPayload(BaseModel):
    email: EmailStr
    password: str
    


class SignupPayload(BaseModel):
    email: EmailStr
    password: str
        
