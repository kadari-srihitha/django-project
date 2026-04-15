from django.db import models

# Create your models here.
class doctor(models.Model):
 name = models.CharField(max_length=200,null=True,blank=True)
 specialization = models.CharField(max_length=20,null=True,blank=True)
 def __str__(self):
        return self.name