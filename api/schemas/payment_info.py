from typing import Optional
from pydantic import BaseModel
# If you want to nest order: from .order import Order

class PaymentInfoBase(BaseModel):
    card_number: Optional[str] = None
    payment_type: Optional[str] = None
    transaction_status: Optional[str] = None
    order_id: int

class PaymentInfoCreate(PaymentInfoBase):
    order_id: int  # Ensure required for creation

class PaymentInfoUpdate(BaseModel):
    card_number: Optional[str] = None
    payment_type: Optional[str] = None
    transaction_status: Optional[str] = None
    order_id: Optional[int] = None

class PaymentInfo(PaymentInfoBase):
    id: int

    class ConfigDict:
        from_attributes = True
