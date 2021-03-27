from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    university_id = models.CharField(max_length=10)
    semester = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.university_id