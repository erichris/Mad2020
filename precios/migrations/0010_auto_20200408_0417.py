# Generated by Django 3.0.5 on 2020-04-08 09:17

from django.db import migrations, models
import precios.storage


class Migration(migrations.Migration):

    dependencies = [
        ('precios', '0009_auto_20200408_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textures',
            name='img',
            field=models.ImageField(storage=precios.storage.OverwriteStorage(), upload_to='Textures'),
        ),
    ]
