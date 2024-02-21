"""Tables

Revision ID: ec1097a39d65
Revises: 17088b4584b1
Create Date: 2024-02-21 01:03:32.175728

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec1097a39d65'
down_revision: Union[str, None] = '17088b4584b1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
