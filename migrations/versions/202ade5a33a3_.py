"""empty message

Revision ID: 202ade5a33a3
Revises: a4ffbd2d8f86
Create Date: 2022-07-02 21:23:49.770278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '202ade5a33a3'
down_revision = 'a4ffbd2d8f86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post_user', sa.Column('post_game', sa.String(length=150), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post_user', 'post_game')
    # ### end Alembic commands ###
