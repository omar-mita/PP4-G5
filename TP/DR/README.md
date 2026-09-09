# Proyecto DR

Aplicación web desarrollada con Django. La guía principal está en [../../README.md](../../README.md) y [../../INSTALACION.md](../../INSTALACION.md).

## Ejecutar el proyecto en otra computadora

1. Instalar Python 3.11 o una versión más reciente.
2. Abrir una terminal en la carpeta de este proyecto.
3. Crear un entorno virtual local:

   ```powershell
   python -m venv .venv
   ```

4. Activarlo:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

5. Instalar las dependencias desde la raíz del repositorio:

   ```powershell
   pip install -r ..\..\requirements.txt
   ```

6. Iniciar la aplicación:

   ```powershell
   python manage.py runserver
   ```

7. Abrir `http://127.0.0.1:8000/` en el navegador.

## Git

Los entornos virtuales, cachés de Python y configuraciones locales de editores están excluidos en `.gitignore`. No deben incluirse en commits: cada persona crea su propio entorno con los pasos anteriores.

La base de datos `db.sqlite3` y la carpeta `media/` no están ignoradas, por lo que se incluirán si se agregan al repositorio.
