from sqlalchemy import Boolean, Column, Integer, String

from app.database import Base


# this is how our database will look like

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False)