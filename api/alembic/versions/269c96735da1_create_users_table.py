"""create users table

Revision ID: 269c96735da1
Revises: 
Create Date: 2022-11-24 08:36:25.809942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '481b1e04c901'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
    create table users (
        id serial primary key,
        username text not null unique,
        email text not null unique,
        password text
    );
    """)


def downgrade() -> None:
    op.execute("drop table users;")
