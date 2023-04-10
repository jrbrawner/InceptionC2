from fastapi import APIRouter, Depends, HTTPException
from src.dependencies import get_db
from sqlalchemy.orm import Session
from src.beacon import services
from src.beacon.schemas import Beacon
from typing import Union

router = APIRouter()

@router.post('/beacon', response_model=Union[Beacon, str], tags=['Beacon'])
def create_beacon(name: str, db: Session = Depends(get_db)):
    result = services.create_beacon(db, name)
    if result is None:
        raise HTTPException(400, 'Error in creating beacon.')
    return result

@router.get('/beacon', response_model=list[Beacon], tags=['Beacon'])
def get_all_beacons(db: Session = Depends(get_db)):
    """Get all beacons in the database."""
    result = services.get_all_beacons(db)
    if result is None:
        raise HTTPException(400, 'Error in retrieving beacons.')
    return result

