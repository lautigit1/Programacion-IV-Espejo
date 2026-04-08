"""Creación inicial de la tabla products.

Revision ID: 20260407_01
Revises:
Create Date: 2026-04-07

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "20260407_01"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "products",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nombre", sa.String(length=255), nullable=False),
        sa.Column("descripcion", sa.String(length=2000), nullable=False),
        sa.Column("precio", sa.Float(), nullable=False),
        sa.Column("stock", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_products_nombre"), "products", ["nombre"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_products_nombre"), table_name="products")
    op.drop_table("products")
