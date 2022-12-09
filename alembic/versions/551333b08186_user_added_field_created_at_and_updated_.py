"""user added field created_at and updated_at.

Revision ID: 551333b08186
Revises: 90909d88d7e1
Create Date: 2022-12-07 22:07:08.911687
"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "551333b08186"
down_revision = "90909d88d7e1"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
    )
    op.add_column(
        "users",
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "updated_at")
    op.drop_column("users", "created_at")
    # ### end Alembic commands ###