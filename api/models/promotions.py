from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promo_code = Column(String(100), unique=True, nullable=False)
    expiration_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    discount = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')

    orders = relationship("Order", back_populates="promotion")