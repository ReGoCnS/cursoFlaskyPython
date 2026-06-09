from flask import Blueprint, render_template, request,redirect,url_for
from task import models
from my_app.task import operation

taskRoute = Blueprint('task',__name__,url_prefix='/task')
task_list=['tarea1', 'tarea2', 'tarea3']


@taskRoute.route('/')
def index():
    #operation.create("tareaaa")
    return render_template('dashboard/task/index.html',task=task_list)


@taskRoute.route('/<int:id>')
def show(id:int):
    return 'Show '+str(id)

@taskRoute.route('/delete/<int:id>')
def delete(id:int):
    del task_list[id]
    return redirect(url_for('task.index'))

@taskRoute.route('/create', methods=('GET','POST'))
def create():
    #print(request.form.get('task'))
    task=request.form.get('task')
    if task is not None:
        task_list.append(task)
        return redirect('/task')
    return render_template('dashboard/task/create.html')

@taskRoute.route('/update/<int:id>', methods=('GET','POST'))
def update(id:int):
    task=request.form.get('task')
    if task is not None:
        task_list[id]=task
    return render_template('dashboard/task/update.html')