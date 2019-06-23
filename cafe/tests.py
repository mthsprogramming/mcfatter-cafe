from django.test import TestCase
from . import forms
from django.contrib.auth.models import User
import datetime


class RegisterViewTests(TestCase):
    def sample_form_data(self):
        return {'username': 'test', 'password1': 'testing123',
                                                      'password2': 'testing123', 'first_name': 'Tester',
                                                      'last_name': 'McTest', 'email': 'test@test.com',
                                                      'birth_date': '2017-02-15', 'phone_number': '123-456-7890',}


    def test_forms(self):
        form = forms.SignUpForm(data=self.sample_form_data())
        self.assertTrue(form.is_valid())

    def test_birth_date_field(self):
        form = forms.SignUpForm(data=self.sample_form_data())
        form.is_valid()
        self.assertEquals(datetime.date(year=2017,month=2,day=15), form.cleaned_data['birth_date'])

class LoginViewTests(TestCase):
    def setUp(self):
        self.credentials = {
            'username' : 'testuser',
            'password' : 'secret',}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        # Logged in now

        self.assertTrue(response.context['user'].is_active)
