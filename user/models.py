from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"

    email = models.CharField(max_length=256, default='')
    profile = models.ImageField(upload_to="images/", null=True, blank=True)
