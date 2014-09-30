from flask import *
from flask.ext.sqlalchemy import SQLAlchemy
from sched.models import Base
from sched.forms import AppointmentForm
from sched.models import Appointment

import doctest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sched.db'

# Use Flask-SQLAlchemy for its engine and session
# configuration. Load the extension, giving it the app object,
# and override its default Model class with the pure
# SQLAlchemy declarative Base class.
db = SQLAlchemy(app)
db.Model = Base


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


@app.route('/appointments/<int:appointment_id>/edit/',
           methods=['GET', 'POST'])
def appointment_edit(appointment_id):
    """
    Muestra el formulario para editar una cita en especifico
    >>> appointment_edit(1)
    'Form to edit appointment #1.'
    """
    return 'Form to edit appointment #{0}.'.format(appointment_id)


@app.route('/appointments/create/', methods=['GET', 'POST'])
def appointment_create():
    """
    Provide HTML form to create a new appointment.
    """
    form = AppointmentForm(request.form)
    if request.method == 'POST' and form.validate():
        appt = Appointment()
        form.populate_obj(appt)
        print("Start: {}".format(appt.start))

        db.session.add(appt)
        db.session.commit()
        # Success. Send user back to full appointment list.
        return redirect(url_for('appointment_list'))
    # Either first load or validation error at this point.
    return render_template('appointment/edit.html', form=form)


@app.route(
    '/appointments/<int:appointment_id>/delete/',
    methods=['DELETE'])
def appointment_delete(appointment_id):
    """
    Muestra el formulario para borrar una cita en especifico
    """
    raise NotImplementedError('DELETE')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    doctest.testmod()
    app.run('0.0.0.0', 5000)
