from fastapi import Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.token import get_token_by_value
from app.db.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def verify_token_header(
    authorization: str = Header(...), db: Session = Depends(get_db)
):
    """
    Expects an Authorization header in the format: "Bearer <token>"
    and validates it against tokens stored in the database.
    """
    try:
        scheme, token_value = authorization.split()
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization header format",
        )

    if scheme.lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token scheme"
        )

    token_obj = get_token_by_value(db, token_value)
    if not token_obj:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid"
        )

    return token_obj
