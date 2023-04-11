from sqlalchemy.orm import Session
from src.beacon.models import Beacon
import socket

def create_beacon(db: Session, name: str) -> Beacon:
    """Create a beacon based on user parameters."""
    if db.query(Beacon).filter(Beacon.name == name).first() == None:
        beacon = Beacon(
            name=name,
            hostname=None,
            ip=None,
            port=None,
        )
        db.add(beacon)
        db.commit()
        return beacon
    return 'Beacon exists with that name.'

def get_all_beacons(db: Session) -> list[Beacon]:
    """Return all beacons in the database."""
    beacons = db.query(Beacon).all()
    return beacons

PAYLOADS FOLDER
TEMPLATES
NC PAYLOAD