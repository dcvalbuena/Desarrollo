# Generated by Django 3.2.7 on 2021-10-06 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogo', '0005_lugar'),
    ]

    operations = [
        migrations.AddField(
            model_name='lugar',
            name='num_lugar',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='Servicios_Adicionales',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]