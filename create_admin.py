import os
import django

# 1. Configuración del entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ConsultorioProject.settings')
django.setup()

from django.contrib.auth import get_user_model

def create_or_update_admin():
    User = get_user_model()
    
    # Datos que me proporcionaste
    username = 'ottonmq'
    email = 'ottonmq@gmail.com'
    password = 'otto1979'

    try:
        # 2. Busca al usuario o lo crea si no existe
        user, created = User.objects.get_or_create(
            username=username, 
            defaults={'email': email}
        )

        # 3. Actualiza la contraseña y asegura que sea superusuario
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        if created:
            print(f"¡Éxito! El superusuario '{username}' ha sido creado.")
        else:
            print(f"El usuario '{username}' ya existía. Se ha actualizado su contraseña.")
            
    except Exception as e:
        print(f"Ocurrió un error al crear el admin: {e}")

if __name__ == "__main__":
    create_or_update_admin()
