from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models_vehicle import Vehicle
from schemas_vehicle import VehicleCreate, VehicleOut


router = APIRouter()

@router.post("/vehicles", response_model=VehicleOut)
def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    db_vehicle = Vehicle(**vehicle.dict())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

@router.get("/vehicles", response_model=list[VehicleOut])
def list_vehicles(db:Session = Depends(get_db)):
    return db.query(Vehicle).all()

