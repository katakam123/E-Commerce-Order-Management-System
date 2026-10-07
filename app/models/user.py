from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    hashed_password = Column(String(255), nullable=False)

    role = Column(
        String(20),
        nullable=False,
        default="customer"
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

    # Customer -> Cart (one-to-one)
    cart = relationship(
        "Cart",
        back_populates="customer",
        uselist=False,
        cascade="all, delete-orphan"
    )

    # Customer -> Addresses (one-to-many)
    addresses = relationship(
        "Address",
        back_populates="customer",
        cascade="all, delete-orphan"
    )

    # Customer -> Orders (one-to-many)
    orders = relationship(
        "Order",
        back_populates="customer"
    )

    # Customer -> Reviews (one-to-many)
    reviews = relationship(
        "Review",
        back_populates="customer",
        cascade="all, delete-orphan"
    )