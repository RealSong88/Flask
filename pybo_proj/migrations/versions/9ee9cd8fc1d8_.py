"""empty message

Revision ID: 9ee9cd8fc1d8
Revises: a1e1a5974fab
Create Date: 2020-11-05 18:04:35.904469

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ee9cd8fc1d8'
down_revision = 'a1e1a5974fab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('user_id', sa.Integer(), server_default='1', nullable=True))
    op.create_foreign_key(None, 'question', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'question', type_='foreignkey')
    op.drop_column('question', 'user_id')
    # ### end Alembic commands ###
