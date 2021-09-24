from django.db import models
    
class API(models.Model):
    legajo = models.IntegerField()
    id = models.IntegerField( primary_key=True)
    desc_larga = models.CharField(max_length=100)     
    importe = models.FloatField()
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)