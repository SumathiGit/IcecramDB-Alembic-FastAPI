"""create link table

Revision ID: 1a237ec17b2d
Revises: 98530823a346
Create Date: 2021-10-19 18:04:20.204484

"""
from alembic import op
from sqlalchemy import ForeignKey
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a237ec17b2d'
down_revision = '98530823a346'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'link',
        sa.Column('branch_id', sa.Integer, ForeignKey('branch.id'), primary_key=True),
        sa.Column('icecream_id', sa.Integer, ForeignKey('icecream.id'), primary_key=True),
    )


def downgrade():
    pass
