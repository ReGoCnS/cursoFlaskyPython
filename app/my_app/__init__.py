from flask import Flask
from my_app.task.controller import taskRoute
from my_app.config import Devconfig

app = Flask(__name__)
app.register_blueprint(taskRoute)

app.config.from_object(Devconfig)
# app.debug=True

@app.route('/')
def hola_mundo()-> str:
    return 'Hola desde Flask 2!'
