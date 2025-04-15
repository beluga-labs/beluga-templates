import datetime
import uuid

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Token(Base):
    __tablename__ = "tokens"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    token = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    description = Column(String, nullable=True)

    user_id = Column(String, ForeignKey("users.id"), nullable=True)

    user = relationship("User", back_populates="tokens")
