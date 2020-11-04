from django.test import TestCase
from accounts.models import User

class TestModels(TestCase):

    def setUp(self):
        self.user0 = User.objects.create(
            username = 'Test User',
            email = 'a@b.com',
            password = 'test123456'
        )

    def test_user_saved_accurately(self):
        self.assertEquals(self.user0.username, 'Test User')
        self.assertEquals(self.user0.email, 'a@b.com')
        self.assertEquals(self.user0.password, 'test123456')
        