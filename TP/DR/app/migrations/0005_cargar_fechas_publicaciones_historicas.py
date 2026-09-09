from datetime import datetime
from zoneinfo import ZoneInfo

from django.db import migrations


FECHAS_PUBLICACION = {
    1:  datetime(2026, 8, 10, 10, 15),
    2:  datetime(2026, 8, 11, 14, 40),
    3:  datetime(2026, 8, 13, 9, 20),
    4:  datetime(2026, 8, 15, 17, 5),
    5:  datetime(2026, 8, 17, 11, 30),
    6:  datetime(2026, 8, 19, 16, 10),
    7:  datetime(2026, 8, 21, 12, 50),
    8:  datetime(2026, 8, 23, 18, 25),
    9:  datetime(2026, 8, 25, 10, 5),
    10: datetime(2026, 8, 27, 15, 35),
    11: datetime(2026, 8, 29, 13, 15),
    12: datetime(2026, 8, 31, 19, 10),
    13: datetime(2026, 9, 1, 9, 45),
    14: datetime(2026, 9, 2, 14, 20),
    15: datetime(2026, 9, 3, 11, 55),
    16: datetime(2026, 9, 4, 16, 30),
    17: datetime(2026, 9, 6, 12, 10),
    18: datetime(2026, 9, 7, 18, 5),
}


def cargar_fechas(apps, schema_editor):
    Animal = apps.get_model('app', 'Animal')
    zona = ZoneInfo('America/Argentina/Buenos_Aires')

    for animal_id, fecha in FECHAS_PUBLICACION.items():
        Animal.objects.filter(
            id=animal_id,
            fecha_publicacion__isnull=True,
        ).update(fecha_publicacion=fecha.replace(tzinfo=zona))


def quitar_fechas(apps, schema_editor):
    Animal = apps.get_model('app', 'Animal')
    Animal.objects.filter(id__in=FECHAS_PUBLICACION.keys()).update(fecha_publicacion=None)


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_animal_fechas_reporteria'),
    ]

    operations = [
        migrations.RunPython(cargar_fechas, quitar_fechas),
    ]
