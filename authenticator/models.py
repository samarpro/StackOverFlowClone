from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomModelManager

# Create your models here.
class CustomUser(AbstractUser):
    # making username field dissapper - override
    username = None
    # making email field unique -override
    email = models.EmailField(verbose_name="Email is Here",unique=True)

    # This var is responsible for uniquely identifying user
    # overridding it to make email as unique identifier
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[] 


    objects = CustomModelManager()

    def __str__(self):
        return self.email




