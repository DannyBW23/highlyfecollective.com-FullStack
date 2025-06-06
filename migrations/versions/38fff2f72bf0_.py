"""empty message

Revision ID: 38fff2f72bf0
Revises: 3d61d3e1c852
Create Date: 2023-08-14 14:27:28.422847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38fff2f72bf0'
down_revision = '3d61d3e1c852'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pics_6', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('pics_7', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('pics_8', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('pics_9', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('text_input12', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('text_input13', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('text_input14', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('text_input15', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('text_input16', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('text_input17', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('text_input18', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('text_input19', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('text_input19')
        batch_op.drop_column('text_input18')
        batch_op.drop_column('text_input17')
        batch_op.drop_column('text_input16')
        batch_op.drop_column('text_input15')
        batch_op.drop_column('text_input14')
        batch_op.drop_column('text_input13')
        batch_op.drop_column('text_input12')
        batch_op.drop_column('pics_9')
        batch_op.drop_column('pics_8')
        batch_op.drop_column('pics_7')
        batch_op.drop_column('pics_6')

    # ### end Alembic commands ###
