"""Repository data-access operations for the User model."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import User


class UserRepository:
    """Provide data-access operations for users."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_id(self, user_id: int) -> User | None:
        """Return a user by primary key, or None when not found."""

        statement = select(User).where(User.id == user_id)
        return self._session.scalar(statement)

    def get_by_email(self, email: str) -> User | None:
        """Return a user by email, or None when not found."""

        statement = select(User).where(User.email == email)
        return self._session.scalar(statement)

    def create(self, email: str, display_name: str) -> User:
        """Create and flush a user without committing the transaction."""

        user = User(
            email=email,
            display_name=display_name,
        )
        self._session.add(user)
        self._session.flush()
        return user

    def update_display_name(
        self,
        user: User,
        display_name: str,
    ) -> User:
        """Update a user's display name and flush without committing."""

        user.display_name = display_name
        self._session.flush()
        return user

    def delete(self, user: User) -> None:
        """Delete a user without committing the transaction."""

        self._session.delete(user)
        self._session.flush()
