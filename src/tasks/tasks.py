from win10toast import ToastNotifier  # type: ignore

from .celery import app


@app.task
def notify_task(task_id: int):
    toaster = ToastNotifier()
    toaster.show_toast(
        "Иди работай дура",
        f"Задача {task_id}",
        duration=5,
        threaded=True,
    )
