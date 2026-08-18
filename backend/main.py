from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from pydantic import BaseModel
from sqlmodel import select
from backend.database import create_db_and_tables, SessionDep
from backend.models import Task

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root(session: SessionDep) -> list[Task]:
    tasks = session.exec(select(Task)).all()
    return tasks


@app.get("/tasks/{task_id}")
def read_item(task_id: int, session: SessionDep):
    task = session.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.post("/tasks/")
def create_task(task: Task, session: SessionDep):
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task, session: SessionDep):
    task = session.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    for attr in ['task_name', 'status']:
        setattr(task, attr, getattr(updated_task, attr))
    session.commit()
    session.refresh(task)
    return task


@app.patch("/tasks/{task_id}")
def update_task_status(task_id: int, status: bool, session: SessionDep):
    task = session.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task.status = status
    session.commit()
    session.refresh(task)
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, session: SessionDep):
    task = session.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)
    session.commit()
    return {"message": "Task deleted"}