"""empty message

Revision ID: 52b3bfa3e205
Revises: 09e49c66e61f
Create Date: 2020-11-05 16:18:34.407928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52b3bfa3e205'
down_revision = '09e49c66e61f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
