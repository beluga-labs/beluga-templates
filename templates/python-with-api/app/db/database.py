from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.settings import settings

DATABASE_URL = settings.DATABASE_URL
if not DATABASE_URL:
    raise Exception("DATABASE_URL not set in settings!")

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
