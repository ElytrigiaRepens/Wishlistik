from sqlalchemy.orm import Mapped, mapped_column

from models import BaseModel


class TestBaseModel:
    @staticmethod
    def test_base_model_tablename_inferrence() -> None:
        class PytestTablenameInferrence(BaseModel, kw_only=True):
            id: Mapped[int] = mapped_column(primary_key=True)

        assert PytestTablenameInferrence.__tablename__ == 'pytest_tablename_inferrences'

    @staticmethod
    def test_base_model_preserves_explicit_tablename() -> None:
        class PytestExplicitTablename(BaseModel, kw_only=True):
            __tablename__: str = 'explicit_model_name'
            id: Mapped[int] = mapped_column(primary_key=True)

        assert PytestExplicitTablename.__tablename__ == 'explicit_model_name'
