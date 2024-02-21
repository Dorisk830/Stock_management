"""products

Revision ID: bd2ba59fb424
Revises: ecba8c9b210e
Create Date: 2024-02-21 01:38:50.631870

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd2ba59fb424'
down_revision: Union[str, None] = 'ecba8c9b210e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
