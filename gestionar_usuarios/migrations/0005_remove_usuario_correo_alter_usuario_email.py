# Generated by Django 5.1 on 2024-08-28 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionar_usuarios', '0004_remove_usuario_nombre_remove_usuario_rol_de_usuario_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='correo',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
