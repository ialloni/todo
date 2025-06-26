from session import db_session

from models.base import Base


def setup_database():
    Base.metadata.create_all(db_session.engine)
    return db_session
