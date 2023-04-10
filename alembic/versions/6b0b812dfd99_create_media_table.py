"""create media table

Revision ID: 6b0b812dfd99
Revises: b75152be748d
Create Date: 2023-04-03 03:46:50.347441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b0b812dfd99'
down_revision = 'b75152be748d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('media', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('media', 'content')
    pass
