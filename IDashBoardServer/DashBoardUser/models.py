from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class DashBoardUser(models.Model):
    user = models.OneToOneField(User)
    department = models.CharField(max_length=100, null=True)
    phone = models.PositiveIntegerField(null=True)
