from django.contrib import admin
from .models import Paciente

# Configuración del encabezado
admin.site.site_header = "Dr. René Quant Matus"
admin.site.site_title = "Clínica de Ultrasonido"

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    # Solo campos que SI existen en tu modelo
    list_display = ('nombre', 'dui', 'telefono', 'tipo_ultrasonido')
    search_fields = ('nombre', 'dui')
    list_filter = ('tipo_ultrasonido', 'nacionalidad')
