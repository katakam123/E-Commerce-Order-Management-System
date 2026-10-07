"""rename password hash column

Revision ID: 249cd8828614
Revises: 73228c4d0638
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "249cd8828614"
down_revision: Union[str, Sequence[str], None] = "73228c4d0638"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "users",
        "password_hash",
        existing_type=sa.String(length=255),
        new_column_name="hashed_password",
        existing_nullable=False,
    )


def downgrade() -> None:
    op.alter_column(
        "users",
        "hashed_password",
        existing_type=sa.String(length=255),
        new_column_name="password_hash",
        existing_nullable=False,
    )