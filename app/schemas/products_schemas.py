from pydantic import BaseModel
from typing import Optional, List
from app.schemas.category_schemas import CategoryOut

class ProductBase(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    category_ids: Optional[List[int]] = None

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    name: str
    price: float
    description: Optional[str] = None
    categories: Optional[List[CategoryOut]] = None

    model_config = {
      'from_attributes': True
    }
