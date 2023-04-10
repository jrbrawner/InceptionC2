from pydantic import BaseModel

class Beacon(BaseModel):
    id : int
    name : str
    status : bool

    class Config:
        orm_mode = True