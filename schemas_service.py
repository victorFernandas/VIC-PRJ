from pydantic import BaseModel
from datetime import date


class ServiceCreate(BaseModel):
    vehicle_id : int
    agent_id : int
    service_type : str
    service_date : date
    status : str



class ServiceOut(ServiceCreate):
    id : int
    class Config:
        orm_mode = True


        