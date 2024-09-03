"""generate company table

Revision ID: d31fdf67054a
Revises: 27d563bd6e1c
Create Date: 2024-08-20 14:24:35.281726

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from schemas.company import Mode
from uuid import uuid4
from datetime import datetime, timezone


# revision identifiers, used by Alembic.
revision: str = 'd31fdf67054a'
down_revision: Union[str, None] = '27d563bd6e1c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    company_table = op.create_table(
        "companies",
        sa.Column("id", sa.UUID, primary_key=True, nullable=False),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("description", sa.String, nullable=True),
        sa.Column("mode", sa.Enum(Mode), nullable=False, default=Mode.ACTIVE),
        sa.Column('rating', sa.SmallInteger, default=0),
        sa.Column("created_at", sa.DateTime),
        sa.Column("updated_at", sa.DateTime),
        )
    
    # Update User Table
    op.add_column("users", sa.Column("company_id", sa.UUID, nullable=True))
    op.create_foreign_key("fk_user_company", "users", "companies", ["company_id"],['id'])
    
    # Data seed for some companies
    op.bulk_insert(company_table, [
        {
            "id": uuid4(),
            "name": "NashTech", 
            "description": "A very large cooperation",
            "rating": 3,
            "mode": Mode.ACTIVE,
            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.now(timezone.utc)
        },
        {
            "id": uuid4(),
            "name": "FPT Software", 
            "description": "A company from Viet Nam",
            "rating": 1,
            "mode": Mode.INACTIVE,
            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.now(timezone.utc)
        },
        {
            "id": uuid4(),
            "name": "KMS Technology", 
            "description": "Description for KMS Technology",
            "rating": 2,
            "mode": Mode.ACTIVE,
            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.now(timezone.utc)
        }
    ])


def downgrade() -> None:
    op.drop_constraint("fk_user_company", "users", type_="foreignkey")
    op.drop_column("users", "company_id")
    op.drop_table("companies")
    op.execute("DROP TYPE mode;")
