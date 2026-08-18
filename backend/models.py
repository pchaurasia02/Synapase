from sqlmodel import Field, SQLModel


class Task(SQLModel, table=True):
    task_id: int = Field(default=None, primary_key=True)
    task_name: str
    status: bool = False