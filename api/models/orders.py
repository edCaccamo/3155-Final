from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    status = Column(String(100))
    total_price = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')
    customer_id = Column(Integer, ForeignKey("customers.id"))
    promotion_id = Column(Integer, ForeignKey("promotions.id"), nullable=True)
    # id, order_date, status, total_price, customer_id, promotion_id

    order_details = relationship("OrderDetail", back_populates="order")
    customer = relationship("Customer", back_populates="orders")
    promotion = relationship("Promotion", back_populates="orders")
    payment_info = relationship("PaymentInfo", back_populates="order")