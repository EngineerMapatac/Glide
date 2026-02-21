from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskEventBase(BaseModel):
    task_id: str
    previous_status: Optional[str] = None
    new_status: str
    assigned_to: Optional[str] = None

class TaskEventCreate(TaskEventBase):
    pass

class TaskEventResponse(TaskEventBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True