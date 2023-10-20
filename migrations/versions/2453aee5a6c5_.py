"""empty message

Revision ID: 2453aee5a6c5
Revises: 
Create Date: 2023-10-20 19:23:35.126989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2453aee5a6c5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    op.create_table('favs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('color', sa.String(length=80), nullable=True),
    sa.Column('pet', sa.String(length=80), nullable=True),
    sa.Column('meal', sa.String(length=80), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favs')
    op.drop_table('user')
    # ### end Alembic commands ###