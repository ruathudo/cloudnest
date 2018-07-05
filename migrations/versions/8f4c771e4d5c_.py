"""empty message

Revision ID: 8f4c771e4d5c
Revises: 
Create Date: 2018-07-06 02:44:24.794452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f4c771e4d5c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('avatar', sa.String(length=100), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###