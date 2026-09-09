# Guía de instalación y ejecución

## Requisitos

- Windows 10/11 (o un sistema compatible con Python).
- Python 3.11 o superior instalado y disponible como comando `python`.
- Git, si se va a clonar el repositorio.

## Instalación desde GitHub

```powershell
git clone https://github.com/omar-mita/PP4-G5.git
cd PP4-G5\TP\DR
```

## Crear el entorno virtual

El entorno virtual es local para cada computadora y no se descarga desde GitHub:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación, se puede ejecutar Django directamente con `.\.venv\Scripts\python.exe` o habilitar scripts para el usuario actual:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## Instalar dependencias

```powershell
pip install -r ..\..\requirements.txt
```

Las versiones están fijadas en `requirements.txt` para que todas las personas instalen las mismas dependencias:

- Django 5.2.17
- Django REST Framework 3.18.1
- Pillow 12.3.0

## Comprobar y ejecutar

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py runserver
```

Luego abrir `http://127.0.0.1:8000/`.

Con el entorno activado, también se puede usar `python manage.py check` y `python manage.py runserver`.

## Base de datos y archivos multimedia

El repositorio incluye `TP/DR/db.sqlite3` y `TP/DR/media/` para que la revisión local tenga los datos e imágenes del proyecto escolar. En un proyecto real convendría usar una base de datos y almacenamiento configurados para cada ambiente.

## Qué no se sube a Git

`.gitignore` excluye `.venv`, `venv`, cachés `__pycache__`, archivos `.vs` de Visual Studio, configuraciones de editores, logs y resultados de pruebas. Estos archivos se generan localmente y no son necesarios para ejecutar la aplicación.
