# Starter Code for Building REST APIs with FastAPI

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(title="Task API")

# -------------------------------------------------------
# Task 1 – Health-check route
# -------------------------------------------------------

# TODO: Define a GET / route that returns {"status": "ok", "message": "API is running"}
# @app.get("/")
# def root():
#     ...


# -------------------------------------------------------
# Task 2 – Data model and CRUD routes
# -------------------------------------------------------

# TODO: Define a Task Pydantic model with id, title, and completed fields
# class Task(BaseModel):
#     ...

# In-memory store
tasks: List = []

# TODO: GET /tasks — return all tasks
# @app.get("/tasks")
# def get_tasks():
#     ...

# TODO: POST /tasks — add a new task, return 201 on success
# @app.post("/tasks", status_code=status.HTTP_201_CREATED)
# def create_task(task: Task):
#     ...

# TODO: DELETE /tasks/{task_id} — remove a task by ID, return 404 if not found
# @app.delete("/tasks/{task_id}")
# def delete_task(task_id: int):
#     ...


# -------------------------------------------------------
# Task 3 – Validation and error handling
# -------------------------------------------------------

# TODO: Add Pydantic field constraints to Task (min_length, gt=0)
# TODO: Return HTTP 400 when a task with the same id already exists
# TODO: Use HTTPException for all error responses
# TODO: Visit /docs to verify Swagger UI shows all routes and models

# Run with: uvicorn starter-code:app --reload
