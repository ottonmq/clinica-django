import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ConsultorioProject.settings')
django.setup()

User = get_user_model()

# AQUÍ PON TUS DATOS REALES PARA ENTRAR
mi_usuario = 'ottonmq'          # El nombre que tú quieras
mi_correo = 'ottonmq@gmail.com'  # Tu correo real
mi_clave = 'otto1979'      # Una clave que no olvides

# Esta parte evita el error de duplicado
if not User.objects.filter(username=mi_usuario).exists():
    User.objects.create_superuser(mi_usuario, mi_correo, mi_clave)
    print(f"¡Éxito! Usuario {mi_usuario} creado.")
else:
    # Si ya existe, actualizamos la clave por si acaso se te olvidó
    user = User.objects.get(username=mi_usuario)
    user.set_password(mi_clave)
    user.save()
    print(f"El usuario {mi_usuario} ya existía, pero hemos actualizado su clave.")
