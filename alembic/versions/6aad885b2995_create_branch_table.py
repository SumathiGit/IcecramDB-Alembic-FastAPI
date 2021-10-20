"""create branch table

Revision ID: 6aad885b2995
Revises: 
Create Date: 2021-10-19 17:55:45.564803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6aad885b2995'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'branch',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('branchname', sa.String(50), nullable=False),
        sa.Column('address', sa.Unicode(200)),
    )

def downgrade():
    pass
