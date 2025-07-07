from datetime import datetime

from rich import print
from rich.panel import Panel
from rich.table import Table

from src.models.task import Status
from src.services.task_service import TaskService


class CommandsCLI:
    def _create_task(self, service: TaskService):
        print(Panel('Напишите задачу в формате: "Текст" "Дата ( Jun 1 2005 1:33PM )"'))
        text = str(input("Введите задачу: "))
        date_str = str(input("Введите дату: "))
        try:
            scheduled_date = datetime.strptime(date_str, "%b %d %Y %I:%M%p")
            service.create_task(text=text, scheduled_date=scheduled_date)
        except ValueError:
            print("Неправильно введенные данные")
            return

    def _list_tasks(self, service: TaskService):
        tasks = service.list_task()
        table = Table(title="Список команд", style="blue")
        table.add_column("ID", style="cyan", justify="center")
        table.add_column("Text", style="cyan", justify="center")
        table.add_column("Date", style="cyan", justify="center")
        table.add_column("Status", style="cyan", justify="center")

        for task in tasks:
            status_symbol = "✔" if task.status == Status.completed else "✝"
            table.add_row(
                str(task.oid), task.text, str(task.scheduled_date), status_symbol
            )
        print(table)

    def _delete_task(self, service: TaskService):
        oid = int(input("Введите id: "))
        service.delete_task(oid)

    def _update_status(self, service: TaskService):
        oid = int(input("Введите id: "))
        service.update_task_status(oid)
        return

    def _update_task(self, service: TaskService):
        oid = int(input("Введите id: "))
        text = str(input("Введите текст задачи: "))
        date_str = str(input("Введите дату: "))
        service.update_task_text(oid=oid, text=text)
        service.update_task_date(oid=oid, scheduled_date=date_str)
