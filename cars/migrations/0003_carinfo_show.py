# Generated by Django 3.2.6 on 2021-08-11 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20210811_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='carinfo',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]
