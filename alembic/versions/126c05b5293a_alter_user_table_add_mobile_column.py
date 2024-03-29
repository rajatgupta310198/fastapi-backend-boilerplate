"""alter user table add mobile column.

Revision ID: 126c05b5293a
Revises: 324a031227c2
Create Date: 2023-07-16 00:34:26.128412
"""
import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = "126c05b5293a"
down_revision = "324a031227c2"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("mobile", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "mobile")
    # ### end Alembic commands ###
