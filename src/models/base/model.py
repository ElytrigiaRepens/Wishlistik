"""Base class for all Wishlistik models."""

from typing import Any

from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

from utils import classname_to_tablename


class BaseModel(MappedAsDataclass, DeclarativeBase, repr=False, kw_only=True):
    """Base class for all Wishlistik models."""

    def __init_subclass__(cls, **kwargs: Any) -> None:  # noqa: ANN401
        """Add tablename if not present."""

        if getattr(cls, '__tablename__', None) is None:
            cls.__tablename__ = classname_to_tablename(cls.__name__)
        super().__init_subclass__(**kwargs)
