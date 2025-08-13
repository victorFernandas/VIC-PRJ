from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from database import Base

Base = declarative_base()


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key= True, index= True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    agent_id = Column(Integer, ForeignKey("users.id"))
    service_type = Column(Integer, ForeignKey("users.id"))
    service_date = Column(Date)
    status = Column(String)


