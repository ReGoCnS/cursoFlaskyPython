from flask import Flask, render_template, request
from my_app.config import DevConfig
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevConfig)

# Inicializamos SQLAlchemy
db = SQLAlchemy(app)

from my_app.task.models import Task

with app.app_context():
    db.create_all()

from my_app.util.template_filter import text_to_upper
app.add_template_filter(text_to_upper)

@app.route('/')
def hola_mundo():
    name = request.args.get('name', 'Desarrolloxd')
    return render_template('index.html', task=name, name=name)

# controlador al final para registrar las rutas de vistas
from my_app.task.controller import taskRoute
app.register_blueprint(taskRoute)