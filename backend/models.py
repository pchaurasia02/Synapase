from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import FastAPI

class Task(SQLModel, table=True):
    id: int = Field(primary_key=True)
    task_name: str
    completed: bool = False