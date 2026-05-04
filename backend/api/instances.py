from fastapi import APIRouter, Depends
from sqlalchemy.orm import session
from db.database import SessionLocal
from schemas.instance import InstanceCreate,InstanceResponse
from crud.instance import create_instance
from schemas.instance import InstanceAction
from services.aws_ec2 import start_instance,stop_instance


router = APIRouter()


# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/instances", response_model=InstanceResponse)
def add_instance(data: InstanceCreate, db: session = Depends(get_db)):
    return create_instance(db, data)

@router.post("/instances/start")
def start_ec2(data: InstanceAction):
    return start_instance(data.instance_id)

@router.post("/instance/stop")
def stop_ec2(data:InstanceAction):
    return stop_instance(data.instance_id)