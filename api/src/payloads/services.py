from sqlalchemy.orm import Session
from src.payloads.models import Payload
import socket

def create_payload(db: Session, name: str) -> Payload:
    """Create a beacon based on user parameters."""
    if db.query(Payload).filter(Payload.name == name).first() == None:
        payload = Payload(
            name=name,
        )
        db.add(payload)
        db.commit()
        return payload
    return 'Payload exists with that name.'

def get_all_beacons(db: Session) -> list[Payload]:
    """Return all beacons in the database."""
    payloads = db.query(Payload).all()
    return payloads
