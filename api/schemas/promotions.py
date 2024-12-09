from datetime import datetime
from typing import Optional, List, Annotated
from pydantic import BaseModel, condecimal

#for formatting price
ConDecimal4_2 = Annotated[float, condecimal(max_digits=4, decimal_places=2)]

class PromotionBase(BaseModel):
    promo_code: str
    expiration_date: datetime
    discount: ConDecimal4_2 = 0.00

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(PromotionBase):
    promo_code: Optional[str] = None
    expiration_date: Optional[datetime] = None
    discount: Optional[ConDecimal4_2] = None

class Promotion(PromotionBase):
    id: int

    class Config:
        from_attributes = True