# Generated by Django 4.2 on 2024-09-19 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionar_proveedor', '0001_initial'),
        ('gestionar_productos', '0004_alter_producto_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='productos_proveedor', to='gestionar_proveedor.proveedor'),
        ),
    ]
