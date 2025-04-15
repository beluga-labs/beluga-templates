from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.crud.token import create_token, delete_token, get_token_by_id
from app.db.database import SessionLocal
from app.schemas.token import Token

router = APIRouter(prefix="/tokens", tags=["tokens"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Token)
def create_new_token(request: Request, db: Session = Depends(get_db)):
    """
    Creates a new token and stores it in the database.
    """
    token_obj = create_token(db)
    return token_obj


@router.get("/{token_id}", response_model=Token)
def read_token(token_id: int, request: Request, db: Session = Depends(get_db)):
    """
    Retrieves token information by token ID.
    """
    token_obj = get_token_by_id(db, token_id)
    if not token_obj:
        raise HTTPException(status_code=404, detail="Token not found")
    return token_obj


@router.delete("/{token_id}")
def remove_token(token_id: int, request: Request, db: Session = Depends(get_db)):
    """
    Deletes a token from the database by token ID.
    """
    token_obj = get_token_by_id(db, token_id)
    if not token_obj:
        raise HTTPException(status_code=404, detail="Token not found")
    delete_token(db, token_id)
    return {"detail": "Token successfully deleted"}
