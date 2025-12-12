from typing import Optional, List
from pydantic import BaseModel

class PizzaBase(BaseModel):
    name: str
    price: float
    calories: int
    category: str



class PizzaCreate(PizzaBase):
    pass

class PizzaUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None


class Pizza(PizzaBase):
    id: int

    class ConfigDict:
        from_attributes = True