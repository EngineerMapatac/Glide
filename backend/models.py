from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class TaskEvent(Base):
    __tablename__ = "task_events"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(String, index=True)
    previous_status = Column(String)
    new_status = Column(String)
    assigned_to = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())