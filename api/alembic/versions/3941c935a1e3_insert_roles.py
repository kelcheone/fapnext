"""insert roles

Revision ID: 3941c935a1e3
Revises: 2d8360fae38a
Create Date: 2022-11-24 08:49:08.785875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ece871602084'
down_revision = '2d8360fae38a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
    insert into roles (name) values ('ROLE_USER');
    insert into roles (name) values ('ROLE_MODERATOR');
    insert into roles (name) values ('ROLE_ADMIN');
    """)


def downgrade() -> None:
    op.execute("""
    delete from roles where name in ('ROLE_USER', 'ROLE_MODERATOR', 'ROLE_ADMIN');
    """)
