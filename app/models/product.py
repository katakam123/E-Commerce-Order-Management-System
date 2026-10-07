from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    Boolean,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(150),
        nullable=False
    )

    description = Column(
        String(500),
        nullable=True
    )

    price = Column(
        Numeric(10, 2),
        nullable=False
    )

    stock_quantity = Column(
        Integer,
        nullable=False,
        default=0
    )

    category_id = Column(
        Integer,
        ForeignKey("categories.id", ondelete="RESTRICT"),
        nullable=False
    )

    is_active = Column(
        Boolean,
        nullable=False,
        default=True
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

    # Category -> Products
    category = relationship(
        "Category",
        back_populates="products"
    )

    # Product -> CartItems
    cart_items = relationship(
        "CartItem",
        back_populates="product"
    )

    # Product -> OrderItems
    order_items = relationship(
        "OrderItem",
        back_populates="product"
    )

    # Product -> Reviews
    reviews = relationship(
        "Review",
        back_populates="product",
        cascade="all, delete-orphan"
    )