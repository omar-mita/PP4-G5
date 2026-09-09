# PP4-G5 — Proyecto final de PP IV

Aplicación web para la gestión de publicaciones de perros en adopción. El backend está desarrollado con Django y utiliza SQLite para el desarrollo local.

## Estructura

- `TP/DR/`: aplicación Django (`manage.py`, proyecto `DR` y aplicación `app`).
- `TP/DR/app/templates/`: páginas HTML.
- `TP/DR/app/static/`: estilos e imágenes estáticas.
- `TP/DR/media/`: imágenes cargadas por la aplicación.
- `TP/DR/db.sqlite3`: base de datos de desarrollo incluida para facilitar la revisión.
- `requirements.txt`: dependencias de Python.
- `INSTALACION.md`: guía detallada de instalación y solución de problemas.

## Inicio rápido en Windows

Desde la raíz del repositorio (`Trabajo_Final`):

```powershell
cd TP\DR
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r ..\..\requirements.txt
python manage.py check
python manage.py runserver
```

Abrir `http://127.0.0.1:8000/` en el navegador.

Para una guía completa, consultar [INSTALACION.md](INSTALACION.md).

## Notas sobre Git

Los entornos virtuales, cachés, archivos de Visual Studio y configuraciones locales están excluidos mediante `.gitignore`. Cada persona debe crear su propio `.venv`; nunca se comparte el entorno virtual de otra computadora porque contiene rutas locales.
