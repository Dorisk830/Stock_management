"""Add new table for orders

Revision ID: 2c7258a0d338
Revises: 9ca4529c1bd3
Create Date: 2024-02-21 03:39:06.966095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c7258a0d338'
down_revision: Union[str, None] = '9ca4529c1bd3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
