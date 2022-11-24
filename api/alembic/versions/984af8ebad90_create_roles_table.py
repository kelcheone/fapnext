"""create roles table

Revision ID: 984af8ebad90
Revises: 269c96735da1
Create Date: 2022-11-24 08:36:26.950106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ce62b651a8f'
down_revision = '481b1e04c901'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
    create table roles (
        id serial primary key,
        name text not null unique
    );
    """)


def downgrade() -> None:
    op.execute("drop table roles;")
