"""create icecream table

Revision ID: 98530823a346
Revises: 6aad885b2995
Create Date: 2021-10-19 18:01:54.535822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98530823a346'
down_revision = '6aad885b2995'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'icecream',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('icecreamname', sa.String(50), nullable=False),
    )


def downgrade():
    pass
