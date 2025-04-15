from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TokenBase(BaseModel):
    token: str
    description: Optional[str] = None


class TokenCreate(TokenBase):
    pass


class Token(TokenBase):
    id: str
    created_at: datetime

    model_config = {"from_attributes": True}
