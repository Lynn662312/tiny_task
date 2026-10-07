from typing import TypedDict
# 1. input
# 2. output (return what)
# 3. what situation will be error and need to use try exception or raise? or condition/loop?
# 4. did it read or modify the data? (read only or modify)?
class Task(TypedDict):
    id: int
    title: str
    completed: bool

# class Task(self,TypedDict):
#     def __init__(self, id: int, title: str, completed: bool) -> None:
#         self.id = id
#         self.title = title
#         self.completed = completed

#what different with the below (code 3 to 6) different with the def __init__ method in a class?

_tasks: dict[int, Task] = {}
_next_id: int = 1

def complete_task(task_id:int) -> Task:
    task = _tasks.get(task_id)
    if task is None:
        raise ValueError(f"Task with id {task_id} not found.")
    task["completed"] = True
    return task.copy()

def delete_task(task_id: int) ->bool:
    if task_id in _tasks:
        del _tasks[task_id]
        return True
    return False

#input is title, while output generatte by system (id) and also automatically stored it as list
def create_task(title: str, completed: bool = False) -> Task:
    global _next_id
    #why gloabal? 
    clean_title = title.strip()
    if not clean_title:
        raise ValueError("Task title cannot be empty.")
    task: Task = {
        "id": _next_id,
        "title": clean_title,
        "completed": completed
    }
    # give dict[key] then return value
    _tasks[_next_id] = task
    _next_id += 1
    return task.copy()

#what is .copy() method? -> use to protect internal data since dict is mutable
def list_tasks() -> list[Task]:
    return [task.copy() for task in _tasks.values()]

# using task id due to its uniqueness, while title is not unique
def get_task(task_id: int) -> Task:
    task = _tasks.get(task_id)
    if task is None:
        raise ValueError(f"Task with id {task_id} not found.")
    return task.copy()

task1= create_task("Task 1", completed=True)
task2= create_task("Task 2", completed=False)
print(task1)
print(list_tasks())
print(get_task(1))
# print(get_task(4))
print("\nTasks:")
for task in list_tasks():
    print(task)
sqlTask = create_task(" Study SQL ")
print(sqlTask)
# print(create_task("  "))
print("\nCompleted task:")
sqlTask = complete_task(sqlTask["id"])
print(sqlTask)
task3 = create_task("Read HTTP")
task3["title"] = "I changed smt"
print(get_task(task3["id"]))  # This will print the original title, not "I changed smt" becuase using .copy()


