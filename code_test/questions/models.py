"""_summary_"""

from django.db import models


# Create your models here.
class Employee(models.Model):
    """_summary_"""

    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
