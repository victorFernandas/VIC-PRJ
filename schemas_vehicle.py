from pydantic import BaseModel

class VehicleBase(BaseModel):
    brand : str
    model : str
    status: str


class VehicleCreate(VehicleBase):
    owner_id : int

class VehicleOut(VehicleBase):
    id : int
    class Config:
        orm_mode = True

