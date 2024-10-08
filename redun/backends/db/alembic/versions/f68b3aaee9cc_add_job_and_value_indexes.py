"""add job and value indexes

Revision ID: f68b3aaee9cc
Revises: eb7b95e4e8bf
Create Date: 2024-06-14 18:42:22.604907

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = "f68b3aaee9cc"
down_revision = "eb7b95e4e8bf"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("job", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_job_end_time"), ["end_time"], unique=False)
        batch_op.create_index(batch_op.f("ix_job_start_time"), ["start_time"], unique=False)

    with op.batch_alter_table("value", schema=None) as batch_op:
        batch_op.create_index(batch_op.f("ix_value_type"), ["type"], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("value", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_value_type"))

    with op.batch_alter_table("job", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_job_start_time"))
        batch_op.drop_index(batch_op.f("ix_job_end_time"))

    # ### end Alembic commands ###
