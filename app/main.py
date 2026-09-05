from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Task(BaseModel):
    title: str
    description: str
    priority: str

tasks = []

@app.get("/")
def root():
    return {"message": "DevOps Task Manager is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return task


@app.get("/tasks")
def get_tasks():
    return tasks