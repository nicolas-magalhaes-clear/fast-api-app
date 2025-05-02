from sqlalchemy.orm import declarative_base, Mapped, mapped_column, class_mapper
from datetime import datetime
from typing import Any, Dict

class BaseModel:
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now)

    def to_dict(self) -> Dict[str, Any]:
        return {column.key: getattr(self, column.key) for column in class_mapper(self.__class__).columns}


BaseModel = declarative_base(cls=BaseModel)
