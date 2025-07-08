import time

from rich import print
from rich.progress import track
from rich.table import Table

from src.cli.commands import CommandsCLI
from src.database.session import session_factory
from src.repositories.task_repository import TaskRepository
from src.services.task_service import TaskService
from src.tasks.celery import Scheduler


class TodoCLI(CommandsCLI):
    def interface(self):
        for _ in track(range(100), description="Загрузка..."):
            time.sleep(0.02)
        table = Table(title="Список команд", style="blue")
        table.add_column("ID", style="cyan", justify="center")
        table.add_column("Команда", style="cyan", justify="center")

        table.add_row("1", "Добавить задачу")
        table.add_row("2", "Список задач")
        table.add_row("3", "Удалить задачу")
        table.add_row("4", "Выполнить задачу")
        table.add_row("5", "Обновить задачу")
        table.add_row("6", "Выйти")

        print(table)

    def run(self):
        while True:
            self.interface()
            choices_handler = {
                1: self._create_task,
                2: self._list_tasks,
                3: self._delete_task,
                4: self._update_status,
                5: self._update_task,
            }
            choice = int(input())
            if choice == 6:
                print("Удачи!")
                break
            handler = choices_handler.get(choice)
            if handler is None:
                print("Неправильный выбор")
                continue
            scheduler = Scheduler()

            with session_factory.begin() as session:
                task_repo = TaskRepository(session)
                task_service = TaskService(task_repo, scheduler)
                handler(task_service)
            scheduler.commit()
