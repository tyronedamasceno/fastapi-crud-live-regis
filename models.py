from sqlalchemy import Column, String, Integer

from database import Base


class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    kind = Column(String, nullable=True)
