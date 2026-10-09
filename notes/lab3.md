for the folder, need to create a file named : __init__.py (dont know why)

TaskCreate = request body schema/input model
TaskOut = response schema/output model
payload = parsed JSON body object
response_model = output contract shown in /docs and used by FastAPI
HTTPException = convert service/API problem into HTTP error response

Why POST for creation instead of GET?
ans: POST is used because creating a task changes server-side state. GET should be used for safe read-only retrieval and should not intentionally modify server data.

Why 201 for successful creation?
ans: 201 Created means the request succeeded and a new resource was created. For POST /tasks, the server creates a new task, so 201 is more suitable than normal 200.

Why 404 when /tasks/999 does not exist?
ans:The route /tasks/{task_id} exists, but task id 999 is not found in the task store. So the API should return 404 Not Found.

What happens if task_id is "abc"? Which layer rejects it?
ans: FastAPI/Pydantic rejects it before the route function runs, because task_id is declared as int. "abc" cannot be converted into an integer, so FastAPI returns a validation error, usually 422.

What is Content-Type telling the server?
ans: Content-Type tells the server what format the request body is in. For example, Content-Type: application/json means the request body is JSON.

status code:204 mean success but no response body