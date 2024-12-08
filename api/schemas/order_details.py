from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# Assuming Sandwich is defined in api/schemas/sandwiches.py
from .sandwiches import Sandwich


class OrderDetailBase(BaseModel):
    amount: int


class OrderDetailCreate(OrderDetailBase):
    order_id: int
    sandwich_id: int


class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    sandwich_id: Optional[int] = None
    amount: Optional[int] = None


class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    sandwich: Optional[Sandwich] = None

    class Config:
        from_attributes = True
