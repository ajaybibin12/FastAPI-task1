from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

#Creating models for users

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True,nullable=False)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    phone_number=Column(String)