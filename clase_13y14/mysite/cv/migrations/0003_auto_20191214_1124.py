# Generated by Django 2.2.7 on 2019-12-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20191214_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitacion',
            name='descripcion',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
