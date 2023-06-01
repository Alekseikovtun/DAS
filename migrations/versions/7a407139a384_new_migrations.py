"""new migrations

Revision ID: 7a407139a384
Revises: f1d140ff0497
Create Date: 2023-05-04 16:54:46.519387

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7a407139a384'
down_revision = 'f1d140ff0497'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('drone', 'access_key')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('drone', sa.Column('access_key', mysql.VARCHAR(length=64), nullable=True))
    # ### end Alembic commands ###
