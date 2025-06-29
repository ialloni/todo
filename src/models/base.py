from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    oid: Mapped[int] = mapped_column(primary_key=True)
