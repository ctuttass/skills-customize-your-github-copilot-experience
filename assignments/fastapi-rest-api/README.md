# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a fully functional REST API using the FastAPI framework, practising route definitions, request/response models with Pydantic, and basic CRUD operations.

## 📝 Tasks

### 🛠️ Create Your First FastAPI App

#### Description
Set up a FastAPI application and define a simple health-check route to confirm the server is running.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn (`pip install fastapi uvicorn`)
- Create a FastAPI app instance using `FastAPI()`
- Define a `GET /` route that returns `{"status": "ok", "message": "API is running"}`
- Start the server with `uvicorn main:app --reload` and verify the response in the browser or with `curl`

### 🛠️ Define a Data Model and CRUD Routes

#### Description
Model a simple resource (e.g. a `Task`) using Pydantic and implement Create, Read, and Delete endpoints for it.

#### Requirements
Completed program should:

- Define a `Task` Pydantic model with at least three fields: `id` (int), `title` (str), and `completed` (bool)
- Store tasks in an in-memory list (no database required)
- Implement the following routes:
  - `GET /tasks` — returns all tasks
  - `POST /tasks` — accepts a JSON body and adds a new task; returns the created task with status code `201`
  - `DELETE /tasks/{task_id}` — removes the task with the given ID; returns `404` if not found
- Example `POST /tasks` request body:
  ```json
  { "id": 1, "title": "Learn FastAPI", "completed": false }
  ```

### 🛠️ Add Input Validation and Error Handling

#### Description
Extend the API to validate incoming data and return meaningful error responses when something goes wrong.

#### Requirements
Completed program should:

- Use Pydantic field constraints to validate that `title` is not empty (`min_length=1`) and `id` is positive (`gt=0`)
- Return a `400` error with a descriptive message when a task with the same `id` already exists
- Use FastAPI's `HTTPException` for all error responses
- Confirm that FastAPI's automatic docs at `/docs` (Swagger UI) correctly reflect all routes, models, and possible responses
