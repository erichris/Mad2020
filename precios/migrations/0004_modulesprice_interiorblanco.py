# Generated by Django 3.0.5 on 2020-04-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('precios', '0003_auto_20200407_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulesprice',
            name='interiorBlanco',
            field=models.BooleanField(default=False),
        ),
    ]
