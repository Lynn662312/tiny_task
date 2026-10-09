from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
#load from other files
from app import task_service

app = FastAPI(title="Tiny Task", description="Lab for self-learning")
#request body (input) client just need to send title (as str) and the length (1 to 120)
class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)

#response body (output) (api return to the client)
class TaskOut(BaseModel):
    id:int
    title:str
    completed:bool

class TaskUpdate(BaseModel):
    title:str |None = Field(default=None,min_length=1,max_length=120)
    completed:bool |None = None

#payload = parsed JSON(Request) body object
# response_model = output contract shown in /docs and used by FastAPI (follow the schema)
@app.post("/tasks",response_model=TaskOut,status_code=status.HTTP_201_CREATED)
def create_task(payload:TaskCreate):
    try:
        return task_service.create_task(payload.title)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

@app.get("/tasks",response_model=list[TaskOut])
def list_tasks():
    return task_service.list_tasks()

#/tasks/aaa is invalid because "aaa" cannot become an integer. FastAPI/Pydantic rejects it at the API validation layer before your function logic should run.
@app.get("/tasks/{task_id}",response_model=TaskOut)
def get_task(task_id:int):
    task = task_service.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404,detail="Task not found")
    return task

@app.patch("/tasks/{task_id}",response_model=TaskOut,status_code=status.HTTP_200_OK)
def update_task(task_id:int,payload:TaskUpdate):
    task = task_service.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404,detail="Task not found")
    try:
        if payload.title is not None:
            task_service.update_task_title(task_id,payload.title)

        if payload.completed is not None:
            task_service.update_task_completed(task_id,payload.completed)
    except ValueError as exc:
        raise HTTPException(status_code=400,detail=str(exc)) from exc
    updated_task = task_service.get_task(task_id)
    return updated_task

@app.delete("/tasks/{task_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int):
    deleted = task_service.delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
    return None




@app.get("/health")
def health() -> dict[str,str]:
    return {"status": "ok"}

@app.get("/")
def home() -> dict[str,str]:
    return {"message": "Welcome to Tiny Task!"}

# @app.post("/name")
# def create_name() -> dict[str,str]:
#     return {"name": "Tiny Task"}

