from typing import List
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import BaseModel
from app.models.product_category import product_category
from app.models.category import Category

class Product(BaseModel):
    __tablename__ = "products"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    categories: Mapped[List["Category"]] = relationship(
        secondary=product_category,
        back_populates="products"
    )
    
    def __repr__(self) -> str:
        return f"<Product {self.to_dict()}>"
    