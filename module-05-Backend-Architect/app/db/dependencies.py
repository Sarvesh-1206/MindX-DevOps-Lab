"""FastAPI dependencies for database sessions."""

from collections.abc import Generator

from sqlalchemy.orm import Session

from app.db.database import SessionLocal


def get_db() -> Generator[Session, None, None]:
    """Yield a database session and close it after request processing."""

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
