from django.db import models

# Supposedly it's easier to use AbstractUser instead of AbstractBaseUser?
from django.contrib.auth.models import AbstractUser
from .models import models

# Create your models here.

class CustomUser(AbstractUser):
    # track age of user themselves, not age of model
    age = models.PositiveIntegerField(default=0)





