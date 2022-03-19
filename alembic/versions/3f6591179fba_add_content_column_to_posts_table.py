"""Add content column to posts table

Revision ID: 3f6591179fba
Revises: 3b57d1447279
Create Date: 2022-03-13 20:25:09.674378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f6591179fba'
down_revision = '3b57d1447279'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
