"""new migrations

Revision ID: 4b54443c4cad
Revises: cd62f8db5d2f
Create Date: 2023-03-31 09:02:20.576530

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4b54443c4cad'
down_revision = 'cd62f8db5d2f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('flight', sa.Column('flight_status', sa.VARCHAR(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('flight', 'flight_status')
    # ### end Alembic commands ###
