from typing import Iterable
from django.db import models

# Create your models here.


class test(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()

    def save(self, *args,**kwargs):
        super(test,self).save(*args,**kwargs)
        print(self.name)
        
        