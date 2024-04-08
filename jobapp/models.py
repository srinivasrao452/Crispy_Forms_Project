
from django.db import models

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=50, help_text='enter your full name')
    emp_code = models.CharField(max_length=3)
    mobile = models.BigIntegerField(unique=True)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname



from django.contrib.auth.models import User
from django.utils import timezone
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table='post'

















