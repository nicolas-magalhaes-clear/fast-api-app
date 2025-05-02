from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import BaseModel

class Product(BaseModel):
    __tablename__ = "products"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)