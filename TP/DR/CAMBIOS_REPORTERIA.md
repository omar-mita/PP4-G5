# AdoptDog - versión con adopciones y reportería

Esta versión agrega una evolución funcional sobre el proyecto original sin eliminar los datos existentes.

## Funcionalidades incorporadas

- Estado **Adoptado** para cerrar correctamente una publicación cuando el perro encuentra hogar.
- Acción **Marcar como adoptado** desde Mis publicaciones, con pantalla de confirmación.
- Registro automático de **fecha de publicación**, **fecha de adopción** y **fecha de baja**.
- Las publicaciones adoptadas o dadas de baja dejan de poder editarse o cambiarse nuevamente.
- Nueva opción **Reportes** en el menú de usuarios autenticados.
- Indicadores generales: total de publicaciones, disponibles, adoptados, bajas y tasa de adopción.
- Reporte mensual con cantidad de publicaciones generadas, perros adoptados y publicaciones dadas de baja.
- Historial detallado de publicaciones con estado y fechas de cierre.
- Se mantiene el historial anterior sin inventar fechas: las 18 publicaciones originales aparecen como **históricas sin fecha registrada**.

## Base de datos

La migración `0004_animal_fechas_reporteria.py` ya fue aplicada a la base incluida en este ZIP.
Si se utiliza el código con otra base de datos, ejecutar:

```bash
python manage.py migrate
```

## Validación

Se agregaron pruebas automáticas para verificar:

- Registro de adopción y fecha.
- Ocultamiento del perro adoptado en el inicio.
- Registro de fecha de baja.
- Protección para que un usuario no modifique publicaciones ajenas.
- Renderizado y datos principales del reporte.

## Datos históricos de demostración

Para facilitar la demostración de la reportería, las 18 publicaciones preexistentes recibieron fechas de publicación ficticias distribuidas entre el 10/08/2026 y el 07/09/2026. Esta carga se realiza mediante la migración `0005_cargar_fechas_publicaciones_historicas.py` y no modifica el estado de las publicaciones ni inventa fechas de adopción o baja.
