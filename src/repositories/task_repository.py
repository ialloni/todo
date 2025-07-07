from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.task import Task

from .base import BaseRepository


class TaskRepository(BaseRepository[Task]):
    def __init__(self, session: Session) -> None:
        super().__init__(session, Task)

    def update_status(self, oid: int) -> None:
        self.update_by_id(oid, {"status": "completed"})

    def completed_list(self) -> Sequence[Task]:
        stmt = select(Task).filter_by(status="completed")
        res = self.session.execute(stmt)
        return res.scalars().all()
