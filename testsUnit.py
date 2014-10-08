import unittest
import sched.app as app
import sched.models as models
import sched.forms as forms
from datetime import datetime
from datetime import timedelta


class testModelApponintment(unittest.TestCase):

    def test_appointment_Duration(self):
        now = datetime.now()
        appt = models.Appointment(
            title='Prueba Unitaria', start=now,
            end=now + timedelta(seconds=1800),
            allday=False)
        self.assertEqual(1800, appt.duration)
        self.assertNotEqual(1801, appt.duration)

    def test_appointment_Repre_(self):
        now = datetime.now()
        appt = models.Appointment(
            title='Prueba Unitaria Repre', start=now,
            end=now + timedelta(seconds=1800),
            allday=False)
        self.assertNotEqual('<Appointment: 3>', appt.__repr__())


class testModelUser(unittest.TestCase):

    def test_user_password(self):
        user = models.User(name="Usuario Nuevo", email="email2@cimat.mx")
        user._set_password("thepassword")
        self.assertNotEqual(user._get_password, "thepassword")
        self.assertEqual(True, user.check_password("thepassword"))
        self.assertNotEqual(True, user.check_password("thepassword2"))

    def test_user_status(self):
        user = models.User(name="Usuario Nuevo", email="email2@cimat.mx")
        user._set_password("thepassword")
        self.assertNotEqual(user.get_id, 0)
        self.assertNotEqual(user.is_active, False)
        self.assertNotEqual(user.is_anonymous, True)
        self.assertNotEqual(user.is_authenticated, False)

    def test_user_authenticate(self):
        user, authenticate = models.User.authenticate(
            app.db.session.query, "email@cimat.mx", "thepassword")
        self.assertNotEqual(authenticate, False)
        self.assertNotEqual(user.name, "Usuario")


class testForm(unittest.TestCase):

    def test_form_Appt(self):
        form = forms.AppointmentForm()
        self.assertEqual(
            '<input id="title" name="title" type="text" value="">', str(form.title))
        self.assertEqual(
            '<input id="start" name="start" type="text" value="">', str(form.start))
        self.assertEqual(
            '<input id="end" name="end" type="text" value="">', str(form.end))
        self.assertEqual(
            '<input id="allday" name="allday" type="checkbox" value="y">', str(form.allday))
        self.assertEqual(
            '<input id="location" name="location" type="text" value="">', str(form.location))
        self.assertEqual(
            '<textarea id="description" name="description"></textarea>', str(form.description))

    def test_form_Login(self):
        form = forms.LoginForm()
        self.assertEqual(
            '<input id="username" name="username" type="text" value="">', str(form.username))
        self.assertEqual(
            '<input id="password" name="password" type="password" value="">', str(form.password))


class testApp(unittest.TestCase):

    def setUp(self):
        self.appt = app.app.test_client()

    def test_appt_list(self):
        response = self.appt.get("/appointments")
        print("response")
        # print(response.data)
        self.assertEquals(response.status_code, 301)
        assert 'Redirecting' in response.data

    def test_login(self):
        response = self.appt.get("/login/?next=%2Fappointments%2F")
        # print(response.data)


class testDelete(unittest.TestCase):
    pass

# def test_error_delete(self):
#   self.assertRaises(NotImplementedError, m.appointment_delete, 1)

if __name__ == '__main__':
    unittest.main()
