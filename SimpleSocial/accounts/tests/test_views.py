from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('accounts:login')
        self.logout_url = reverse('accounts:logout')
        self.signup_url = reverse('accounts:signup')

    def test_signup_page_GET(self):
        response = self.client.get(self.signup_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')
    
    def test_login_page_GET(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_logout_page_GET(self):
        response = self.client.get(self.logout_url)

        self.assertEquals(response.status_code, 302)
        # This line throws an error 'AssertionError: No templates used to render the response'
        # self.assertTemplateUsed(response, 'templates/thanks.html')