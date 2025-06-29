from src.database.session import session_factory
from src.database.setup import setup_database
from src.models.task import Task
from src.repositories.base import BaseRepository


def main():
    setup_database()
    with session_factory.begin() as session:
        base = BaseRepository(session, Task)
        # base.create({"text": "qweqwe", "scheduled_date": datetime.datetime.now()})
        base.delete_by_id(1)
        res = base.list()
        print(*res)


if __name__ == "__main__":
    main()
