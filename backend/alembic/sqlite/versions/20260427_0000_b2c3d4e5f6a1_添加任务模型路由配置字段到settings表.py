"""添加任务模型路由配置字段到settings表

Revision ID: b2c3d4e5f6a1
Revises: ab12cd34ef56
Create Date: 2026-04-27 00:00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b2c3d4e5f6a1'
down_revision: Union[str, None] = 'ab12cd34ef56'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    connection = op.get_bind()
    result = connection.execute(sa.text("PRAGMA table_info(settings)"))
    columns = [row[1] for row in result]
    if 'task_model_config' not in columns:
        op.add_column('settings', sa.Column('task_model_config', sa.Text(), nullable=True, comment='任务模型路由配置(JSON): {task_type: model_name}'))


def downgrade() -> None:
    op.drop_column('settings', 'task_model_config')
