# Generated by Django 2.2.7 on 2019-12-14 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitacion',
            name='nombre_institucion',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='capacitacion',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='experiencialaboral',
            name='nombre_empresa',
            field=models.CharField(max_length=100),
        ),
    ]
