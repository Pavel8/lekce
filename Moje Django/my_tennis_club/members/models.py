from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(default=None)
    joined_date = models.DateField(default=None)

    def __str__(self):
      return f"{self.firstname} {self.lastname}"