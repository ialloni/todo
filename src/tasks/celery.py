from dataclasses import dataclass
from datetime import datetime

from celery import Celery
from celery.app.task import Task

from src.settings import settings

app = Celery(
    broker=settings.celery_broker_dsn,
)
from .tasks import notify_task


@dataclass
class ScheduledTask:
    task: Task
    args: tuple
    eta: datetime


class Scheduler:
    def __init__(self) -> None:
        self.tasks: list[ScheduledTask] = []

    def add_task(self, task: Task, args: tuple, eta: datetime) -> None:
        scheduled_task = ScheduledTask(task=task, eta=eta, args=args)
        self.tasks.append(scheduled_task)

    def commit(self):
        for task in self.tasks:
            task.task.apply_async(args=task.args, eta=task.eta)
