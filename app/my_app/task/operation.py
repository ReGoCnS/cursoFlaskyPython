from sqlalchemy.orm import Session
from my_app.task import models
from my_app import db

def getByID(id: int):
    #task=db.session.query(models.Task).filter(models.Task.id==id).first()
    task=db.session.query(models.Task).get(id)
    return task


def getAll():
    task= db.session.query(models.Task).all()
    return task

def create(name: str):
    taskdb=models.Task(name=name)
    db.session.add(taskdb)
    db.session.commit()
    db.session.refresh(taskdb)
    return taskdb

def update(id:int, name: str):
    taskdb=getByID(id=id)
    taskdb.name=name
    db.session.add(taskdb)
    db.session.commit()
    db.session.refresh(taskdb)
    return taskdb

def delete(id:int):
    taskdb=getByID(id=id)
    db.session.delete(taskdb)
    db.session.commit()

def pagination(page:int, size:int ):
    models.Task.query.paginate(page, size)