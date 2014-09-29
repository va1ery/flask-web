from flask import *
from flask import make_response
from flask.ext.sqlalchemy import SQLAlchemy
from models import Base

import doctest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sched.db'

# Use Flask-SQLAlchemy for its engine and session
# configuration. Load the extension, giving it the app object,
# and override its default Model class with the pure
# SQLAlchemy declarative Base class.
db = SQLAlchemy(app)
db.Model = Base


@app.route('/object/')
def return_object():
    headers = {'Content-Type': 'text/plain'}    
    status = 404
    t = ('Hefjasd fasdld!', status, headers)
    return make_response(t)


@app.route('/appointments/')
def appointment_list():
    """
    Muestra la lista de las citas
    >>> appointment_list()
    'Listing of all appointments we have.'
    """
    return 'Listing of all appointments we have.'


@app.route('/appointments/<int:appointment_id>/')
def appointment_detail(appointment_id):
    """
    Muestra el detalle de una cita en especifico
    >>> appointment_detail(1)
    'Detail of appointment #1.'
    """
    return 'Detail of appointment #{0}.'.format(appointment_id)


@app.route(
    '/appointments/<int:appointment_id>/edit/',
    methods=['GET', 'POST'])
def appointment_edit(appointment_id):
    """
    Muestra el formulario para editar una cita en especifico
    >>> appointment_edit(1)
    'Form to edit appointment #1.'
    """
    return 'Form to edit appointment #{0}.'.format(appointment_id)


@app.route(
    '/appointments/create/',
    methods=['GET', 'POST'])
def appointment_create():
    """
    Muestra el formulario para crear una cita
    >>> appointment_create()
    'Form to create a new appointment.'
    """
    return 'Form to create a new appointment.'


@app.route(
    '/appointments/<int:appointment_id>/delete/',
    methods=['DELETE'])
def appointment_delete(appointment_id):
    """
    Muestra el formulario para borrar una cita en especifico
    """
    raise NotImplementedError('DELETE')


@app.route('/')
def hello():
    """
    >>> hello()
    'Hello, world!'
    """
    return 'Hello, world!'


if __name__ == "__main__":
    doctest.testmod()
    app.run('0.0.0.0', 5000)
