from fastapi import APIRouter, Depends, HTTPException
from src.dependencies import get_db
from sqlalchemy.orm import Session
from src.payloads import services
from src.payloads.schemas import Payload
from typing import Union

router = APIRouter()

@router.post('/payload', response_model=Union[Payload, str], tags=['Payload'])
def create_payload(name: str, db: Session = Depends(get_db)):
    result = services.create_payload(db, name)
    if result is None:
        raise HTTPException(400, 'Error in creating payload.')
    return result

@router.get('/payload', response_model=list[Payload], tags=['Payload'])
def get_all_payloads(db: Session = Depends(get_db)):
    """Get all payloads in the database."""
    result = services.get_all_payloads(db)
    if result is None:
        raise HTTPException(400, 'Error in retrieving beacons.')
    return result