from pydantic import BaseModel

class Payload(BaseModel):
    id : int
    name : str

    class Config:
        orm_mode = True