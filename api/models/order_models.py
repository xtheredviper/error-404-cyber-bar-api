from pydantic import BaseModel
from typing import List


class OrderItem(BaseModel):
    product: str
    quantity: int


class OrderCreate(BaseModel):
    items: List[OrderItem]


class OrderStatus(BaseModel):
    status: str