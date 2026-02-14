from pydantic import BaseModel, EmailStr
from typing import Optional
class User(BaseModel):
    id: int
    nombre: str
    email: EmailStr

class UserUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None