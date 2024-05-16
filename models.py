import enum
from sqlalchemy import Enum, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Priority(enum.Enum):
    low = 1
    medium = 2
    high = 3


class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String)
    priority: Mapped[Priority] = mapped_column(Enum(Priority))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, description={self.description!r})"

