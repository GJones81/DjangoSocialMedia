from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.views import LoginView, LogoutView

from accounts.views import SignUp


# Create your tests here.

class TestUrls(SimpleTestCase):

    def test_login_url_resolves(self):
        url = reverse('accounts:login')
        
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_logout_url_resolves(self):
        url = reverse('accounts:logout')

        self.assertEquals(resolve(url).func.view_class, LogoutView)

    def test_signup_url_resolves(self):
        url = reverse('accounts:signup')
        
        self.assertEquals(resolve(url).func.view_class, SignUp)
