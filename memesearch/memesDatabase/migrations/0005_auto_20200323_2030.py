# Generated by Django 2.2.6 on 2020-03-23 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memesDatabase', '0004_auto_20200322_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagedescriptions',
            name='image',
        ),
        migrations.RemoveField(
            model_name='textdescriptions',
            name='image',
        ),
        migrations.AddField(
            model_name='imagedescriptions',
            name='word',
            field=models.TextField(default='defaul'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='textdescriptions',
            name='word',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]