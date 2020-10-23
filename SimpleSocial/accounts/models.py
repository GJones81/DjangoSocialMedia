from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        # .username is builtin to the User class from models
        return "@{}".format(self.username)
