# Generated by Django 2.2.6 on 2020-03-22 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memesDatabase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.URLField(),
        ),
    ]
