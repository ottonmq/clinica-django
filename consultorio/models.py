from django.db import models

# Create your models here.
from django.db import models

class Paciente(models.Model):
    # --- Información Personal ---
    nombre = models.CharField(max_length=200)
    edad = models.IntegerField(null=True, blank=True)
    nacionalidad = models.CharField(max_length=100, default='Salvadoreña')
    dui = models.CharField(max_length=20, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    
    # --- Historia Médica ---
    consulta_por = models.CharField(max_length=255, null=True, blank=True)
    enfermedad_actual = models.CharField(max_length=255, null=True, blank=True)
    antecedentes_personales_familiares = models.CharField(max_length=255, null=True, blank=True)
    
    # --- Examen Físico (Signos Vitales) ---
    pa = models.CharField(max_length=20, null=True, blank=True)
    fc = models.CharField(max_length=20, null=True, blank=True)
    fr = models.CharField(max_length=20, null=True, blank=True)
    
    # --- Control de Embarazo ---
    fum = models.DateField(null=True, blank=True)
    fpm = models.DateField(null=True, blank=True)
    fpp = models.DateField(null=True, blank=True)
    amenorrea_semanas = models.IntegerField(default=0)
    amenorrea_dias = models.IntegerField(default=0)

    # --- SECCIÓN ULTRASONIDO (Opciones y Campos Normales) ---
    OPCIONES_ULTRA = [
        ('Obstétrico', 'Obstétrico'),
        ('Pélvico', 'Pélvico'),
        ('Abdominal', 'Abdominal'),
        ('Transvaginal', 'Transvaginal'),
        ('Renal', 'Renal'),
        ('Mama', 'Mama'),
        ('Prostático', 'Prostático'),
    ]
    tipo_ultrasonido = models.CharField(max_length=50, choices=OPCIONES_ULTRA, null=True, blank=True)
    detalle_ultrasonido = models.CharField(max_length=255, null=True, blank=True) # Para hallazgos cortos

    def __str__(self):
        return self.nombre
