"""empty message

Revision ID: 5863d6cb845b
Revises: f218ee707d33
Create Date: 2023-03-30 13:29:04.072449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5863d6cb845b'
down_revision = 'f218ee707d33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('email', sa.VARCHAR(length=255), nullable=True),
    sa.Column('password', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
