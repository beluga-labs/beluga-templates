import secrets

from sqlalchemy.orm import Session

from app.models.token import Token


def create_token(db: Session, user_id: str = None, description: str = None) -> Token:
    """
    Generates a new token, optionally associates it with a user and
    stores it in the database.
    """
    token_value = secrets.token_urlsafe(32)  # Secure, random token
    token_obj = Token(token=token_value, user_id=user_id, description=description)
    db.add(token_obj)
    db.commit()
    db.refresh(token_obj)
    return token_obj


def get_token_by_id(db: Session, token_id: str) -> Token | None:
    return db.query(Token).filter(Token.id == token_id).first()


def delete_token(db: Session, token_id: str) -> None:
    token_obj = get_token_by_id(db, token_id)
    if token_obj:
        db.delete(token_obj)
        db.commit()


def get_token_by_value(db: Session, token_value: str) -> Token | None:
    return db.query(Token).filter(Token.token == token_value).first()
