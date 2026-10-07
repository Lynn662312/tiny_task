#refer to task_service.py
## try my own without ai:
"""
1. class
2. create function , need title
3. get function also check by using id
4. delete function, remove from the list
5. list out
6. change task status
"""
from typing import TypedDict
class Task(TypedDict):
    id: int
    title: str
    completed: bool

tasks: dict[int, Task] ={}
next_id: int =1

#require title as input, then return Task, camnnot empty title (raise error). create the task into the task list
def create_task(title:str) -> Task:
    global next_id
    clean_title = title.strip()
    # if empty title raise error
    if not clean_title:
        raise ValueError("title can't be empty")
    #if not empty, start create new task
    task: Task =  {
        "id": next_id,
        "title": clean_title,
        "completed": False,
    }

    tasks[next_id] = task
    next_id += 1 #increment 1 for next task use
    return task.copy() # use .copy() to protect the data no modified since dict is mutable

def get_task(task_id:int) -> Task | None:
    task = tasks.get(task_id)
    return task.copy() if task else None

def remove_task(task_id:int) -> bool:
    # task = tasks.get(task_id)
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False
    

def list_tasks() -> list[Task]:
    return [task.copy() for task in tasks.values()]

#just get the id then change the status to true
def change_status(task_id:int) -> Task:
    if task_id not in tasks:
        raise ValueError(f"No have this task id {task_id}. pls check again")
    
    task = tasks[task_id]
    task["completed"] = True
    
    return task.copy()

def ask_task_id(prompt:str) -> int:
    while True:
        raw_value = input(prompt).strip()
        try:
            return int(raw_value)
        except ValueError:
            print("pls enter a valid num")

if __name__ == "__main__":
    print("\n")
    print(list_tasks())
    task1 = create_task("wash bacon")
    print(f"create Task: \n{task1}")
    print("\nList task:")
    print(list_tasks())
    task1 = change_status(task1["id"])
    print("\nChange status:")
    print(task1)

    new_task = input("Enter new task title:")
    task2 = create_task(new_task)
    print("\nCreate task:")
    print(task2)

    print("\nCurrent list:")
    for task in list_tasks():
        print(f"\n{task}")

    print("\nDelete function:")
    while True:
        delete_task = ask_task_id("Enter the task id u want delete:")
        delete_task1 = remove_task(delete_task)
        if delete_task1:
            print(f"Task delete: {delete_task1}")
            break

        print(f"No task with this id:{delete_task}. pls try again")

    print("\nCurrent list:")
    for task in list_tasks():
        print(f"\n{task}")

    print("\nUpdate function")
    while True:
    #since the up variable already have the id
        update_task_status = ask_task_id("\nEnter the task id u want update the status:")
        try:
            update_task1 = change_status(update_task_status)
            print(f"Update task status: {update_task1}")
            break  
        except ValueError as e:
            print(e)
            print("pls try again")

    print("\nCurrent list:")
    for task in list_tasks():
        print(f"{task}")
