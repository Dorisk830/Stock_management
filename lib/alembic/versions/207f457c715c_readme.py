"""README

Revision ID: 207f457c715c
Revises: 2c7258a0d338
Create Date: 2024-02-21 03:39:37.064771

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '207f457c715c'
down_revision: Union[str, None] = '2c7258a0d338'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
