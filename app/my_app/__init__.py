from flask import Flask, render_template, request
from my_app.task.controller import taskRoute
from my_app.config import Devconfig

app = Flask(__name__)
app.register_blueprint(taskRoute)

app.config.from_object(Devconfig)
# app.debug=True

@app.route('/')
def hola_mundo(): #-> str
    name = request.args.get('name','Desarrolloxd')
    return render_template('index.html',task=name,name=name)
    return 'Hola desde Flask 2!'
