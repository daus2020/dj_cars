# Generated by Django 4.0.5 on 2023-07-13 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculomodel',
            name='marca',
            field=models.CharField(choices=[('FOR', 'Ford'), ('FIA', 'Fiat'), ('CHE', 'Chevrolet'), ('TOY', 'Toyota')], default='Ford', max_length=20),
        ),
    ]
