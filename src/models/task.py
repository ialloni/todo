import datetime
import enum

from sqlalchemy import types
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Status(enum.StrEnum):
    completed = "completed"
    scheduled = "scheduled"


class Task(Base):
    __tablename__ = "Tasks"

    text: Mapped[str] = mapped_column(nullable=False)
    scheduled_date: Mapped[datetime.datetime] = mapped_column(
        types.DateTime(timezone=True)
    )
    status: Mapped[Status] = mapped_column(types.Enum(Status), default=Status.scheduled)

    def __str__(self) -> str:
        return f"Task({self.text=}, {self.scheduled_date=}, {self.status=})"
