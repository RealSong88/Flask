"""empty message

Revision ID: a1e1a5974fab
Revises: 52b3bfa3e205
Create Date: 2020-11-05 17:59:59.157846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1e1a5974fab'
down_revision = '52b3bfa3e205'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'question', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'question', type_='foreignkey')
    op.drop_column('question', 'user_id')
    # ### end Alembic commands ###
