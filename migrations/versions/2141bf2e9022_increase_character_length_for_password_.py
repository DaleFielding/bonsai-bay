"""increase character length for password_hash

Revision ID: 2141bf2e9022
Revises: 785ba1d0a241
Create Date: 2024-04-13 19:18:46.148259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2141bf2e9022'
down_revision = '785ba1d0a241'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=256),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)

    # ### end Alembic commands ###
