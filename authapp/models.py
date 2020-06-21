# Create your models here.
from django.db import models
#import uuid
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100)
    #name = models.CharField(max_length=100, unique=False)
    email = models.EmailField(verbose_name='email', unique=True, max_length=225)
    #phone = models.CharField(null=True, max_length=25)
    REQUIRED_FIELDS=['username']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
