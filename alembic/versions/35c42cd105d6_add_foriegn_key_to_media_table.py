"""add foriegn key to media table

Revision ID: 35c42cd105d6
Revises: efc62dff00ca
Create Date: 2023-04-07 09:11:16.230662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35c42cd105d6'
down_revision = 'efc62dff00ca'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('media', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('media_users_fk', source_table="media", referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('media_users_fk', table_name="media")
    op.drop_column('media', 'owner_id')
    pass
