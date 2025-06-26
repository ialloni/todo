import datetime
import enum

from base import Base
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column


class Status(enum.Enum):
    completed = "completed"
    scheduled = "scheduled"


class Task(Base):
    __tablename__ = "Tasks"

    text: Mapped[str] = mapped_column(nullable=False)
    scheduled_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    status: Mapped[Status]
