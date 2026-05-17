from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)

from sqlalchemy.orm import relationship

from api.database.connection import Base


class OrderModel(Base):

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    status = Column(String)

    items = relationship(
        "OrderItemModel",
        back_populates="order"
    )


class OrderItemModel(Base):

    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)

    product = Column(String)

    quantity = Column(Integer)

    total = Column(Float)

    order_id = Column(
        Integer,
        ForeignKey("orders.id")
    )

    order = relationship(
        "OrderModel",
        back_populates="items"
    )