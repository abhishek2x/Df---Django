# Generated by Django 2.1.4 on 2019-07-11 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sem',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], default=1),
        ),
    ]
