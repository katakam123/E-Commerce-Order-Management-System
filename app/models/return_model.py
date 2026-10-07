from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    Numeric,
    String,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database import Base


class ReturnRequest(Base):
    __tablename__ = "return_requests"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    order_id = Column(
        Integer,
        ForeignKey("orders.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    reason = Column(
        Text,
        nullable=False
    )

    status = Column(
        String(20),
        nullable=False,
        default="Requested"
    )

    refund_amount = Column(
        Numeric(10, 2),
        nullable=True
    )

    rejection_reason = Column(
        Text,
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

    order = relationship(
        "Order",
        back_populates="return_request"
    )