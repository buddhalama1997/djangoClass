from django.db import models
from matplotlib import widgets

# Create your models here.
class StudentDetails(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=50)
    stuemail = models.EmailField(max_length=100)