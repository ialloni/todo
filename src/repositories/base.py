from typing import Generic, Optional, Sequence, TypeVar

from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import Session
from sqlalchemy.orm.base import instance_dict

from src.models.base import Base

T = TypeVar("T", bound=Base)


class BaseRepository(Generic[T]):
    def __init__(self, session: Session, model: type[T]) -> None:
        self.session = session
        self.model = model

    def create(self, values: dict) -> None:
        stmt = insert(self.model).values(values)
        self.session.execute(stmt)

    def list(self) -> Sequence[T]:
        stmt = select(self.model)
        res = self.session.execute(stmt)
        return res.scalars().all()

    def get_by_id(self, id: int) -> Optional[T]:
        stmt = select(self.model).filter_by(id=id)
        res = self.session.execute(stmt)
        return res.scalar_one_or_none()

    def delete_by_id(self, id: int) -> None:
        stmt = delete(self.model).filter_by(id=id)
        self.session.execute(stmt)

    def update_by_id(self, id: int, values: dict) -> T:
        stmt = update(self.model).filter_by(id=id).values(values)
        res = self.session.execute(stmt)
        return res.scalar_one()
