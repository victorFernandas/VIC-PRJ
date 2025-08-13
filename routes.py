
'''
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

tasks = []

class Task(BaseModel):
    id : int
    title : str
    description : str

#Get all tasks:
@router.get('/tasks')
def get_tasks():

    if not tasks:
        raise HTTPException(status_code=404 , detail= 'Your tasks were not found')
    return tasks

#Get tasks by task id:
@router.get('/tasks/{task_id}')
def get_tasks_by_id(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
        
#Create a Data:
@router.post('/tasks')
def create_task(task:Task):
    tasks.append(task)

    return task


#Delete a task:

@router.delete('/tasks/{task_id}')
def dete_task(task_id: int):

    for index, task in enumerate(tasks):

        if task.id == task_id:
            tasks.pop(index)

            return {'Message' :' Task deleted successfully'}
        
    raise HTTPException(status_code= 404, detail= ' The task you entered is not found')

#Update Tasks:

@router.put('/tasks/{task_id}')
def update_task(task_id:int, new_task:Task):

    for index, task in enumerate(tasks):
        if task.id == task_id:

            tasks[index] == new_task

            return {'Message' : 'New task is updated'}
        
    return HTTPException(status_code= 404, detail= 'The task you entered is not found')
'''


from fastapi import APIRouter, HTTPException, Query, Depends
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session
from database import SessionLocal, Task as TaskModal


router = APIRouter()

tasks = []

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

class Task(BaseModel):
    id : int
    title : str
    description : str

#Get all tasks:()
@router.get('/tasks')
def get_tasks(limit: Optional[int] = Query(None, description= ' The limit of number of tasks is 5'), search : Optional[str] = Query(None, description='The search results are filtered by the keyword you entered'), db:Session = Depends (get_db())):
    return db.query(TaskModal).all()

#Get tasks by task id:
@router.get('/tasks/{task_id}')
def get_tasks_by_id(task_id: int, db:Session = Depends (get_db())):
    for task in tasks:
        if task.id == task_id:
            return task
    
    raise HTTPException(status_code= 404, detail= 'The task you entered is not found')

#Create a Data:
@router.post('/tasks')
def create_task(task: Task, db:Session = Depends(get_db())):
    db_task = TaskModal(id = task.id, title = task.title, description = task.description)
    db.add (db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

    


#Delete a task:

@router.delete('/tasks/{task_id}')
def delete_task(task_id: int, db:Session= Depends(get_db())):

    for index, task in enumerate(tasks):

        if task.id == task_id:
            tasks.pop(index)

            return {'Message' :' Task deleted successfully'}
        
    raise HTTPException(status_code= 404, detail= ' The task you entered is not found')

#Update Tasks:

@router.put('/tasks/{task_id}')
def update_task(task_id:int, new_task:Task, db:Session= Depends(get_db())):

    for index, task in enumerate(tasks):
        if task.id == task_id:

            tasks[index] == new_task

            return {'Message' : 'New task is updated'}
        
    return HTTPException(status_code= 404, detail= 'The task you entered is not found')
