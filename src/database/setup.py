from src.models.base import Base

from .session import engine


def setup_database():
    Base.metadata.create_all(engine)
