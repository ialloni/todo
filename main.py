from src.cli.interface import TodoCLI
from src.database.setup import setup_database


def main():
    setup_database()
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()
