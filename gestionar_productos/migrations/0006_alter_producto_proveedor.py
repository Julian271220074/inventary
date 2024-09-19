# Generated by Django 4.2 on 2024-09-19 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionar_proveedor', '0002_remove_proveedor_producto'),
        ('gestionar_productos', '0005_producto_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionar_proveedor.proveedor'),
        ),
    ]
