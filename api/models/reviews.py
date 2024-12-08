from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    review_text = Column(String(100), nullable=False)
    score = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')
    review_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))

    customer = relationship("Customer", back_populates="reviews")
    sandwich = relationship("Sandwich", back_populates="reviews")