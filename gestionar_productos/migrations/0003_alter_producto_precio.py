# Generated by Django 5.0.7 on 2024-09-10 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionar_productos', '0002_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=50),
        ),
    ]
