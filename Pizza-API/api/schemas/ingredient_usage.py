from typing import Optional
from pydantic import BaseModel


class IngredientUsageBase(BaseModel):
    pizza_id: int
    ingredient_id: int
    quantity: int


class IngredientUsageCreate(IngredientUsageBase):
    pass


class IngredientUsageUpdate(BaseModel):
    quantity: Optional[int] = None


class IngredientUsage(IngredientUsageBase):
    id: int

    class ConfigDict:
        from_attributes = True