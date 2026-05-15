 # SQLAlchemy models

from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from backend.database.base import Base

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)

    machine_id = Column(String, index=True)
    temperature = Column(Float)
    vibration = Column(Float)

    timestamp = Column(DateTime, default=datetime.utcnow)



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

    hashed_password = Column(String)

    role = Column(String, default="technician")