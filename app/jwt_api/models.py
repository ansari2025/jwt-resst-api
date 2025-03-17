from django.db import models

# Create your models here.
class Logincheck(models.Model):
    username=models.CharField(max_length=50)
    password=models.IntegerField(default=18)
   

    def __str__(self):
        return self.username
