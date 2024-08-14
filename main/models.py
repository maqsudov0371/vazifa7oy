from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.urls import reverse
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=13, blank=True, unique=True, db_index=True)
    auth_code = models.CharField(max_length=6, blank=True) 

    # def get_absolute_url(self):
    #     print(self)
    #     return reverse("main:account", kwargs={"id": self.id})


    def __str__(self) -> str:
        return f"{self.username}"
    

