# Generated by Django 3.0.5 on 2020-04-08 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('precios', '0008_textures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textures',
            name='img',
            field=models.ImageField(upload_to='Textures'),
        ),
    ]