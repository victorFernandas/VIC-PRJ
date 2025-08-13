from pydantic import BaseModel, EmailStr
from enum import Enum

class RoleEnum(str, Enum):
    showroom_owner = "showroom_owner"
    service_agent = "service_agent"
    customer = "customer"


class UserCreate(BaseModel):
    email : EmailStr
    password = str
    role = RoleEnum

class UserLogin(BaseModel):
    email : EmailStr
    password : str

