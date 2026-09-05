from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=500)
    priority: Priority


class Task(TaskCreate):
    id: int
    completed: bool = False


tasks = []


@app.get("/")
def root():
    return {"message": "DevOps Task Manager is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/tasks")
def create_task(task: TaskCreate):
    task_id = len(tasks) + 1

    new_task = Task(
        id=task_id,
        title=task.title,
        description=task.description,
        priority=task.priority,
    )

    tasks.append(new_task)

    return new_task


@app.get("/tasks")
def get_tasks():
    return tasks