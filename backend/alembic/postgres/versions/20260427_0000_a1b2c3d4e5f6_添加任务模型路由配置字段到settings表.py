"""添加任务模型路由配置字段到settings表

Revision ID: a1b2c3d4e5f6
Revises: 9a1b2c3d4e5f
Create Date: 2026-04-27 00:00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1b2c3d4e5f6'
down_revision: Union[str, None] = '9a1b2c3d4e5f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    connection = op.get_bind()
    result = connection.execute(
        sa.text("SELECT 1 FROM information_schema.columns WHERE table_name = 'settings' AND column_name = 'task_model_config'")
    )
    if result.first() is None:
        op.add_column('settings', sa.Column('task_model_config', sa.Text(), nullable=True, comment='任务模型路由配置(JSON): {task_type: model_name}'))


def downgrade() -> None:
    op.drop_column('settings', 'task_model_config')
