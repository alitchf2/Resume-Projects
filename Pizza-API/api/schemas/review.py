from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .customer import BaseModel

class ReviewBase(BaseModel):
    customer_id : int
    rating : int
    text : Optional[str] = None

class ReviewCreate(ReviewBase):
    customer_id : int
    rating : int
    text : str
    pizza_id : int

class ReviewUpdate(BaseModel):
    rating: int
    text: Optional[str] = None
    pizza_id: int

class Review(ReviewBase):
    id : int
    
    class ConfigDict:
        from_attributes = True
