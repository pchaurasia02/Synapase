from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


tasks_db = []


class Task(BaseModel):
    task_id: int
    task_name: str
    status: bool = False


@app.get("/")
def read_root():
    return tasks_db

@app.get("/tasks/{task_id}")
def read_item(task_id: int):
    for existing_task in tasks_db:
        if existing_task.task_id == task_id:
            return existing_task
    return {"error": "Task not found"}

@app.post("/tasks/")
def create_task(task: Task):
    for existing_task in tasks_db:
        if existing_task.task_id == task.task_id:
            return {"error": "Task already exists"}
    tasks_db.append(task)
    return task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for existing_task in tasks_db:
        if existing_task.task_id == task_id:
            tasks_db.remove(existing_task)
            tasks_db.append(updated_task)
            return {"message": "Task updated"}
    return {"error": "Task not found"}

@app.patch("/tasks/{task_id}")
def update_task_status(task_id: int, status: bool):
    for existing_task in tasks_db:
        if existing_task.task_id == task_id:
            existing_task.status = status
            return {"message": "Task status updated"}
    return {"error": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for existing_task in tasks_db:
        if existing_task.task_id == task_id:
            tasks_db.remove(existing_task)
            return {"message": "Task deleted"}
    return {"error": "Task not found"}

