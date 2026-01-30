import os
import django
from django.contrib.auth import get_user_model

# Configurar el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djanjocrud.settings")
django.setup()

def create_superuser():
    User = get_user_model()
    
    # Obtener credenciales de las variables de entorno
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

    if username and password:
        if not User.objects.filter(username=username).exists():
            print(f"Creando superusuario: {username}")
            User.objects.create_superuser(username=username, email=email, password=password)
            print("Superusuario creado exitosamente.")
        else:
            print("El superusuario ya existe. Omitiendo creación.")
    else:
        print("No se encontraron variables de entorno para superusuario. Omitiendo.")

if __name__ == "__main__":
    create_superuser()