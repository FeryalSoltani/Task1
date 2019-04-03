from django.db import models
from .validations import PhoneValidator


class Data(models.Model):
    firstName = models.CharField(max_length=150)
    lastName = models.CharField(max_length=150)
    UserID = models.IntegerField()
    PhoneNum = models.CharField(validators = [PhoneValidator], max_length=20)
    Email = models.EmailField(max_length=150)
    DateTime = models.DateField()
    Address = models.TextField()

    def __str__(self):
        return self.Name
