"""empty message

Revision ID: 029fc8bf52f5
Revises: 1a998771d2ea
Create Date: 2023-03-01 21:40:37.282484

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '029fc8bf52f5'
down_revision = '1a998771d2ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('resume', sa.String(length=500), nullable=False))
        batch_op.add_column(sa.Column('active', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('show_in_list', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('image', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('date_created', sa.DateTime(), nullable=True))
        batch_op.drop_column('info')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('info', mysql.VARCHAR(length=500), nullable=False))
        batch_op.drop_column('date_created')
        batch_op.drop_column('image')
        batch_op.drop_column('show_in_list')
        batch_op.drop_column('active')
        batch_op.drop_column('resume')

    # ### end Alembic commands ###
