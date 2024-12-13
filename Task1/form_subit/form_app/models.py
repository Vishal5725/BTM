from django.db import models

# Create your models here.
class FormData(models.Model):
    name = models.CharField(max_length=100) # user's name
    email = models.EmailField()  # user's email
    submited_dateandtime = models.DateTimeField(auto_now_add=True)  # date and time when submit

    def __str__(self):
        return self.name
