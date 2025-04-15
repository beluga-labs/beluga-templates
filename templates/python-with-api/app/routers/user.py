from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.core.limiter import limiter
from app.core.security import verify_token_header
from app.crud.user import create_user, get_user, get_users
from app.db.database import SessionLocal
from app.schemas.user import User as UserSchema
from app.schemas.user import UserCreate

router = APIRouter(
    prefix="/users", tags=["users"], dependencies=[Depends(verify_token_header)]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[UserSchema])
@limiter.limit("10/minute")
def read_users(
    request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return get_users(db, skip=skip, limit=limit)


@router.get("/{user_id}", response_model=UserSchema)
@limiter.limit("15/minute")
def read_user(request: Request, user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/", response_model=UserSchema)
@limiter.limit("5/minute")
def create_new_user(request: Request, user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)
