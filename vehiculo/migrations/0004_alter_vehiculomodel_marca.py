# Generated by Django 4.0.5 on 2023-07-19 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0003_alter_vehiculomodel_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculomodel',
            name='marca',
            field=models.CharField(choices=[('CHEV', 'Chevrolet'), ('FIAT', 'Fiat'), ('FORD', 'Ford'), ('TOYO', 'Toyota')], default='FOR', max_length=20),
        ),
    ]
