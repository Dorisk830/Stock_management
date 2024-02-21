"""products

Revision ID: 9ca4529c1bd3
Revises: b053a4925615
Create Date: 2024-02-21 02:30:05.488315

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ca4529c1bd3'
down_revision: Union[str, None] = 'b053a4925615'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
