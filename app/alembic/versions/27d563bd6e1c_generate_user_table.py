"""generate user table

Revision ID: 27d563bd6e1c
Revises: dc5701065b39
Create Date: 2024-08-21 09:50:58.739614

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from uuid import uuid4
from datetime import datetime, timezone

from schemas.user import get_password_hash
from settings import ADMIN_DEFAULT_PASSWORD


# revision identifiers, used by Alembic.
revision: str = '27d563bd6e1c'
down_revision: Union[str, None] = 'dc5701065b39'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # User Table
    user_table = op.create_table(
        "users",
        sa.Column("id", sa.UUID, nullable=False, primary_key=True),
        sa.Column("email", sa.String, unique=True, nullable=True, index=True),
        sa.Column("username", sa.String, unique=True, index=True),
        sa.Column("first_name", sa.String),
        sa.Column("last_name", sa.String),
        sa.Column("hashed_password", sa.String),
        sa.Column("is_active", sa.Boolean, default=True),
        sa.Column("is_admin", sa.Boolean, default=False),
        sa.Column("created_at", sa.DateTime),
        sa.Column("updated_at", sa.DateTime)
    )
    op.create_index("idx_usr_fst_lst_name", "users", ["first_name", "last_name"])
    # Update Task Table
    op.add_column("tasks", sa.Column("owner_id", sa.UUID, nullable=True))
    op.create_foreign_key("fk_task_owner", "tasks", "users", ["owner_id"],['id'])

    # Data seed for first user
    op.bulk_insert(user_table, [
        {
            "id": uuid4(),
            "email": "fastapi_tour@sample.com", 
            "username": "fa_admin",
            "hashed_password": get_password_hash(ADMIN_DEFAULT_PASSWORD),
            "first_name": "FastApi",
            "last_name": "Admin",
            "is_active": True,
            "is_admin": True,
            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.now(timezone.utc)
        }
    ])


def downgrade() -> None:
    op.drop_constraint("fk_task_owner", "tasks", type_="foreignkey")
    op.drop_column("tasks", "owner_id")
    op.drop_table("users")