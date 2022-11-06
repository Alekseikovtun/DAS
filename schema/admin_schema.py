from schema.base_schema import BaseSchema
from datetime import datetime


class AdminSchema(BaseSchema):
    id: int
    task_status_id: int
    created_at: datetime
    updated_at: datetime
