from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index = True)
    brand = Column(String)
    model = Column(String)
    status = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    