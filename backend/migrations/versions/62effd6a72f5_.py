"""empty message

Revision ID: 62effd6a72f5
Revises: 
Create Date: 2024-09-16 00:34:38.079126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62effd6a72f5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('whisky',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('distillery', sa.String(length=100), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('region', sa.String(length=50), nullable=True),
    sa.Column('tasted', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('whisky')
    # ### end Alembic commands ###