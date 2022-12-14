"""Add priority again

Revision ID: f2180d7f80db
Revises: 29df5476034c
Create Date: 2022-11-06 14:27:43.472900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2180d7f80db'
down_revision = '29df5476034c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('priority', sa.String(length=20), nullable=True))
    op.drop_column('task_status', 'priority')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task_status', sa.Column('priority', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    op.drop_column('task', 'priority')
    # ### end Alembic commands ###
