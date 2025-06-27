from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

from src.settings import settings

engine = create_engine(settings.get_url, echo=True)
session_factory = sessionmaker(bind=engine, expire_on_commit=False)
