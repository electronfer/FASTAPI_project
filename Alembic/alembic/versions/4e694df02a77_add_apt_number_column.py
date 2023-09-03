"""add apt number column

Revision ID: 4e694df02a77
Revises: 06890b11b2d3
Create Date: 2023-09-03 05:36:11.121856

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e694df02a77'
down_revision: Union[str, None] = '06890b11b2d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('address', sa.Column('apt_num', sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column('address', 'apt_num')
