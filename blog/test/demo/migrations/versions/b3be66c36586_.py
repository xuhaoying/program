"""empty message

Revision ID: b3be66c36586
Revises: b8990189df7c
Create Date: 2019-04-16 11:20:56.421835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3be66c36586'
down_revision = 'b8990189df7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('province',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pname', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('pname')
    )
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cname', sa.String(length=32), nullable=True),
    sa.Column('pid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pid'], ['province.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cname')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('city')
    op.drop_table('province')
    # ### end Alembic commands ###
