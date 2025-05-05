from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import BaseModel
from app.models.product_category import product_category

if TYPE_CHECKING:
    from app.models.product import Product


class Category(BaseModel):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    
    # Relação many-to-many com Product
    products: Mapped[List["Product"]] = relationship(
        secondary=product_category,
        back_populates="categories"
    )
    
    def __repr__(self) -> str:
        return f"<Category {self.name}>"