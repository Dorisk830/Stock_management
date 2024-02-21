"""Models

Revision ID: b053a4925615
Revises: bd2ba59fb424
Create Date: 2024-02-21 02:05:25.459725

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b053a4925615'
down_revision: Union[str, None] = 'bd2ba59fb424'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('supplier',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('supplier_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['supplier_id'], ['supplier.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_category_association',
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_category_association')
    op.drop_table('product')
    op.drop_table('supplier')
    op.drop_table('category')
    # ### end Alembic commands ###