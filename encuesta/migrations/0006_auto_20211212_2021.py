# Generated by Django 3.0.8 on 2021-12-13 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0005_auto_20211212_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuesta',
            name='nombre',
            field=models.CharField(help_text='El nombre del usuario encuestado debe ser único', max_length=50, unique=True),
        ),
    ]
