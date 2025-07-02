import datetime
from typing import Sequence, Union

from src.models.task import Task
from src.repositories.task_repository import TaskRepository

from .utils import is_valid_date


class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def create_task(self, text: str, scheduled_date: datetime.datetime) -> None:
        self.repository.create(
            {
                "text": text,
                "scheduled_date": scheduled_date,
            }
        )

    # GET

    def get_task(self, oid: int) -> Union[Task, None, str]:
        res = self.repository.get_by_id(oid)
        if res is None:
            return "Задача не найдена"
        return res

    def list_task(self) -> Sequence[Task]:
        return self.repository.list()

    # UPDATE

    def update_task_date(self, oid: int, scheduled_date: str) -> Union[Task, str]:
        if is_valid_date(scheduled_date):
            return self.repository.update_by_id(oid, {"scheduled_date": scheduled_date})
        return "Невалидная дата"

    def update_task_text(self, oid: int, text: str) -> Task:
        return self.repository.update_by_id(oid, {"text": text})

    def update_task_status(self, oid: int) -> Task:
        return self.repository.update_status(oid)

    # DELETE

    def delete_task(self, oid: int) -> None:
        self.repository.delete_by_id(oid)
