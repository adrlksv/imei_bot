from sqlalchemy import Column, Integer, String

from src.backend.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    login = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
