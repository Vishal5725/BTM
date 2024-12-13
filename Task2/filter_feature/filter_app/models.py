from django.db import models

# Create your models here.
class Box(models.Model):
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.category} - {self.location}"
