# Generated by Django 3.1.7 on 2021-05-17 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicdb', '0008_auto_20210517_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratings',
            name='cole',
            field=models.IntegerField(default=0),
        ),
    ]
