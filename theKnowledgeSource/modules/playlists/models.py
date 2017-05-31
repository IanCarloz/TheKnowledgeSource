from django.db import models
from modules.recursos.models import Recurso
# Create your models here.
class Playlist(models.Model):

    recurso = models.ForeignKey(Recurso)
    nombre = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre   

