import uuid

from sqlalchemy import Column, Date, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

    tokens = relationship("Token", back_populates="user")
