from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from src.db import Base

class Beacon(Base):
    __tablename__ = "Beacon"
    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String, unique=True)
    status : Mapped[bool] = mapped_column(Boolean, default=False)
    hostname : Mapped[str] = mapped_column(String, nullable=True)
    ip : Mapped[str] = mapped_column(String, nullable=True)
    port : Mapped[int] = mapped_column(Integer, nullable=True)