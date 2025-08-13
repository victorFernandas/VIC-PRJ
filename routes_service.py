from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models_service import Service
from schemas_service import ServiceCreate, ServiceOut


router = APIRouter()


@router.post("/services", response_model=ServiceOut)
def create_service(service: ServiceCreate, db: Session = Depends(get_db)):
    db_service = Service(**service.dict())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service


@router.get("/services", response_model=list[ServiceOut])
def list_services(db:Session = Depends(get_db)):
    return db.query(Service).all()