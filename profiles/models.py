from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    #location = models.CharField(max_length=200,default='my location default', blank=True , null=True)
    #job = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
