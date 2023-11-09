from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Historia(models.Model):
    
    texto_validator = RegexValidator(
        regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$',
        message='Este campo solo debe contener letras.'
    )
    
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=4, null=False)
    fecha=models.DateField(null=False)
    nombre_especialista=models.CharField(max_length=20, null=False, validators=[texto_validator])
    diagnostico=models.TextField()
    procedimiento=models.TextField()
    tratamiento=models.TextField()
    paciente_id=models.IntegerField()
    
