from contextlib import contextmanager

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from ..settings import settings


class DataBaseSession:
    def __init__(self, db_url: str) -> None:
        self.engine = create_engine(url=db_url, echo=True)
        self.fabric_session = sessionmaker(bind=self.engine, expire_on_commit=False)
        self.scoped_session = scoped_session(self.fabric_session)

    @contextmanager
    def get_session(self):
        session = self.scoped_session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


db_session = DataBaseSession(db_url=settings.get_url)
