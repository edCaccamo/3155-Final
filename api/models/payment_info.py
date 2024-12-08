from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class PaymentInfo(Base):
    __tablename__ = "payment_info"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    card_number = Column(String(100), nullable=True)
    payment_type = Column(String(100), nullable=True)
    transaction_status = Column(String(100), nullable=True)
    order_id = Column(Integer, ForeignKey("orders.id"))

    order = relationship("Order", back_populates="payment_info")