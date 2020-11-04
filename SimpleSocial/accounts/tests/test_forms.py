from django.test import TestCase
from accounts.forms import UserCreateForm

class TestForms(TestCase):

    def test_user_create_form_valid(self):
        form = UserCreateForm(data={
            'username': 'Tester',
            'email': 'tester@google.com',
            'password1': 'test123456',
            'password2': 'test123456'
        })

        self.assertTrue(form.is_valid())

    def test_user_create_form_empty(self):
        form = UserCreateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)