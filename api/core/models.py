from django.db import models
from datetime import datetime

class Usuario(models.Model):
    nome = models.CharField(db_index=True, max_length=50,unique=True)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=0)
    username = models.CharField(max_length=200, unique=True)
    datetime = models.DateTimeField(default=datetime.now,blank=True)
    
    def __str__(self):
        return self.nome