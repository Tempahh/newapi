"""add colunms to media table

Revision ID: 7bd1a2977fa4
Revises: 35c42cd105d6
Create Date: 2023-04-10 07:57:11.843675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bd1a2977fa4'
down_revision = '35c42cd105d6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('media', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('media', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('media', 'published')
    op.drop_column('media', 'created_at')
    pass
