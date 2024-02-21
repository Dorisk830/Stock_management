"""Tables

Revision ID: ecba8c9b210e
Revises: ec1097a39d65
Create Date: 2024-02-21 01:08:19.215463

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ecba8c9b210e'
down_revision: Union[str, None] = 'ec1097a39d65'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
