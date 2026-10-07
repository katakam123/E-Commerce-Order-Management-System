from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from app.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    order_number = Column(
        String(50),
        unique=True,
        nullable=False,
        index=True
    )

    customer_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="RESTRICT"),
        nullable=False
    )

    address_id = Column(
        Integer,
        ForeignKey("addresses.id", ondelete="RESTRICT"),
        nullable=False
    )

    subtotal = Column(
        Numeric(10, 2),
        nullable=False
    )

    tax_amount = Column(
        Numeric(10, 2),
        nullable=False
    )

    delivery_charge = Column(
        Numeric(10, 2),
        nullable=False
    )

    grand_total = Column(
        Numeric(10, 2),
        nullable=False
    )

    status = Column(
        String(20),
        nullable=False,
        default="Pending"
    )

    payment_status = Column(
        String(20),
        nullable=False,
        default="Unpaid"
    )

    payment_method = Column(
        String(30),
        nullable=True
    )

    delivered_at = Column(
        DateTime,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # User -> Orders
    customer = relationship(
        "User",
        back_populates="orders"
    )

    # Address -> Orders
    address = relationship(
        "Address",
        back_populates="orders"
    )

    # Order -> Order Items
    items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan"
    )

    # Order -> Payments
    payments = relationship(
        "Payment",
        back_populates="order",
        cascade="all, delete-orphan"
    )

    # Order -> Return Request
    return_request = relationship(
        "ReturnRequest",
        back_populates="order",
        uselist=False,
        cascade="all, delete-orphan"
    )