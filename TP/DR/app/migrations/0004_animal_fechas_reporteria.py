from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_programador_usuario_animal_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='fecha_adopcion',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='fecha_baja',
            field=models.DateTimeField(blank=True, null=True),
        ),
        # Primero se agrega como nullable para no inventar una fecha de creación
        # para las publicaciones que ya existían antes de esta funcionalidad.
        migrations.AddField(
            model_name='animal',
            name='fecha_publicacion',
            field=models.DateTimeField(blank=True, null=True),
        ),
        # Luego se activa auto_now_add para que las nuevas publicaciones sí
        # registren automáticamente su fecha de creación.
        migrations.AlterField(
            model_name='animal',
            name='fecha_publicacion',
            field=models.DateTimeField(auto_now_add=True, blank=True, null=True),
        ),
    ]
