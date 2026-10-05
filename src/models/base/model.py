"""Base class for all Wishlistik models."""

from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass


class BaseModel(MappedAsDataclass, DeclarativeBase, repr=False, kw_only=True):
    """Base class for all Wishlistik models."""

    pass
