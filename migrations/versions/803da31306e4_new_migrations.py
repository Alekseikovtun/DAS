"""new migrations

Revision ID: 803da31306e4
Revises: 4b54443c4cad
Create Date: 2023-03-31 09:36:55.533516

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '803da31306e4'
down_revision = '4b54443c4cad'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('flight', 'flight_status')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('flight', sa.Column('flight_status', mysql.VARCHAR(length=64), nullable=True))
    # ### end Alembic commands ###
