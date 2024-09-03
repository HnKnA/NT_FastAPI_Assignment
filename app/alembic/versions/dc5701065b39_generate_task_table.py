"""generate task table

Revision ID: dc5701065b39
Revises: 
Create Date: 2024-08-20 14:27:34.600536

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from schemas.task import Status


# revision identifiers, used by Alembic.
revision: str = 'dc5701065b39'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tasks",
        sa.Column("id", sa.UUID, primary_key=True, nullable=False),
        sa.Column("summary", sa.String, nullable=False),
        sa.Column("description", sa.String, nullable=True),
        sa.Column('status', sa.Enum(Status), nullable=False, default=Status.PROGRESSED),
        sa.Column('priority', sa.SmallInteger, default=0),
        sa.Column("created_at", sa.DateTime),
        sa.Column("updated_at", sa.DateTime),
        )


def downgrade() -> None:
    op.drop_table("tasks")
    op.execute("DROP TYPE status;")
