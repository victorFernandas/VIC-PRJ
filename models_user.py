from sqlalchemy import Column, String, Integer, Enum
from database import Base
import enum
from pydantic import BaseModel, EmailStr

class RoleEnum(str, enum.Enum):
    showroom_owner = "showroom_owner"
    service_agent = "service_agent"
    customer = "customer"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    email = Column(String, unique = True, index = True)
    password = Column(String)
    role = Column(Enum(RoleEnum))

#Schemas / user.py
