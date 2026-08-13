from django.db import models

class hostel(models.Model):
    name=models.CharField(max_length=40)
    pin=models.IntegerField()
    fee=models.IntegerField()
