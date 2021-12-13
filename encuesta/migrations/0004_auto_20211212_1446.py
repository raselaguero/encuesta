# Generated by Django 3.0.8 on 2021-12-12 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0003_auto_20211212_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuesta',
            name='grado_escolaridad',
            field=models.CharField(choices=[('B', 'BACHILLER'), ('L', 'LICENCIADO'), ('M', 'MASTER'), ('D', 'DOCTOR')], max_length=1),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='nombre',
            field=models.CharField(help_text='El nombre del usuario encuestado debe ser único', max_length=25, unique=True),
        ),
    ]