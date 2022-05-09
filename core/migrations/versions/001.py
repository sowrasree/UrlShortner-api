"""

Revision ID: 0001
Revises:
Create Date: 2020-12-07

"""
import inspect

from alembic import op

current_file_name = inspect.getfile(inspect.currentframe())
file_name_with_extension = current_file_name.split('/')[-1]
version = file_name_with_extension.split('.py')[0]

# revision identifiers, used by Alembic.
revision = version
down_revision = None
# down_revision = str(int(revision) - 1).zfill(4)
branch_labels = None
depends_on = None


def upgrade():
    with open('core/migrations/sql/%s.sql' % revision) as fo:
        sql = fo.read()

    connection = op.get_bind()
    connection.execute(sql)
