from fastapi import FastAPI
from src.db import Base, engine
from src.beacon.router import router as beacon_router

app = FastAPI()
app.include_router(beacon_router)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
