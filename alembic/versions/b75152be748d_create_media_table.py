"""create media table

Revision ID: b75152be748d
Revises: 
Create Date: 2023-03-29 14:14:43.027802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b75152be748d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('media',sa.Column('id', sa.Integer(), nullable=False, primary_key=True)
                    , sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('media')
    pass
