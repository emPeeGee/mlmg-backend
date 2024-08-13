"""update users table

Revision ID: 6c245bb86acb
Revises:
Create Date: 2024-08-13 20:45:54.631529

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "6c245bb86acb"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
        sa.UniqueConstraint("username", name=op.f("uq_users_username")),
    )


def downgrade() -> None:
    op.drop_table("users")
