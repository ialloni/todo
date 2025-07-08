from datetime import datetime
from typing import Optional, Sequence, Union

from src.models.task import Task
from src.repositories.task_repository import TaskRepository
from src.tasks.celery import Scheduler
from src.tasks.tasks import notify_task


class TaskService:
    def __init__(self, repository: TaskRepository, scheduler: Scheduler) -> None:
        self.repository = repository
        self.scheduler = scheduler

    def create_task(self, text: str, scheduled_date: datetime) -> None:
        task = self.repository.create(
            {
                "text": text,
                "scheduled_date": scheduled_date,
            }
        )
        self.scheduler.add_task(notify_task, (task.oid,), scheduled_date)

    # GET
    def get_task(self, oid: int) -> Union[Task, None, str]:
        res = self.repository.get_by_id(oid)
        if res is None:
            return "Задача не найдена"
        return res

    def list_task(self) -> Sequence[Task]:
        return self.repository.list()

    # UPDATE

    def update_task_date(self, oid: int, scheduled_date: str) -> Optional[str]:
        try:
            task_date = datetime.strptime(scheduled_date, "%b %d %Y %I:%M%p")
            self.repository.update_by_id(oid, {"scheduled_date": task_date})
        except ValueError:
            return "Невалидная дата"
        return None

    def update_task_text(self, oid: int, text: str) -> None:
        self.repository.update_by_id(oid, {"text": text})

    def update_task_status(self, oid: int) -> None:
        self.repository.update_status(oid)

    # DELETE

    def delete_task(self, oid: int) -> None:
        self.repository.delete_by_id(oid)
