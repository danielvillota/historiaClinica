from django.db import models

# Create your models here.
class Historia(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=4)
    fecha=models.DateField()
    nombre_especialista=models.CharField(max_length=100)
    diagnostico=models.TextField()
    procedimiento=models.TextField()
    tratamiento=models.TextField()
    paciente_id=models.IntegerField()
    
