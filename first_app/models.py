from django.db import models

# Create your models here.
class studentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    fathers_name = models.CharField(max_length=30)
    address = models.TextField()
    