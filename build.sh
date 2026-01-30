#!/usr/bin/env bash
# exit on error
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Recolectar archivos estáticos
python manage.py collectstatic --no-input

# Migrar la base de datos
python manage.py migrate

# Crear superusuario automáticamente si están las variables
python create_superuser.py