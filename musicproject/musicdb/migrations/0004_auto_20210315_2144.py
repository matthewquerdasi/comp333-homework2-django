# Generated by Django 3.1.7 on 2021-03-15 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicdb', '0003_auto_20210315_2045'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Artists',
            new_name='Songs',
        ),
    ]
