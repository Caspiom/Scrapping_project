"""add server defaults

Revision ID: 5a528a92b188
Revises: f752d37ed952
Create Date: 2026-05-15 18:42:07.894516

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a528a92b188'
down_revision: Union[str, Sequence[str], None] = 'f752d37ed952'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column("sources", "created_at", server_default=sa.func.now())
    op.alter_column("articles", "scraped_at", server_default=sa.func.now())


def downgrade() -> None:
    op.alter_column("sources", "created_at", server_default=None)
    op.alter_column("articles", "scraped_at", server_default=None)
