# Generated by Django 2.1.4 on 2019-07-11 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0007_auto_20190711_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='myimg',
            field=models.ImageField(null=True, upload_to='images\\'),
        ),
    ]
