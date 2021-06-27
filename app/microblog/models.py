from sqlalchemy import Column, String, Integer, Date
from core.database import Base


class TableTrain(Base):
    __tablename__ = "requests_train"
    id = Column(Integer, primary_key=True, unique=True)
    start_station = Column(String)
    finish_station = Column(String)
    date = Column(Date)
