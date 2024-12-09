from datetime import datetime
from typing import Optional, List, Annotated
from pydantic import BaseModel, conint

#for formatting price
ConInt1_5 = Annotated[int, conint(ge=1, le=5)]

class ReviewBase(BaseModel):
    review_text: str
    score: ConInt1_5
    review_date: Optional[datetime] = None
    customer_id: int
    sandwich_id: int

class ReviewCreate(ReviewBase):
    review_text: str
    score: ConInt1_5
    customer_id: int
    sandwich_id: int

class ReviewUpdate(BaseModel):
    review_text: Optional[str] = None
    score: Optional[ConInt1_5] = None
    review_date: Optional[datetime] = None
    customer_id: Optional[int] = None
    sandwich_id: Optional[int] = None

class Review(ReviewBase):
    id: int

    class ConfigDict:
        from_attributes = True
