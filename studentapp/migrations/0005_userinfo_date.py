# Generated by Django 2.2 on 2020-05-03 09:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0004_remove_userinfo_bol_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
