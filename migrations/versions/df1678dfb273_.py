"""empty message

Revision ID: df1678dfb273
Revises: 57b7c32b00b7
Create Date: 2024-05-20 01:33:33.200717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df1678dfb273'
down_revision = '57b7c32b00b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('user_email_key', type_='unique')
        batch_op.drop_column('email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
        batch_op.create_unique_constraint('user_email_key', ['email'])

    # ### end Alembic commands ###