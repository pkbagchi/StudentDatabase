# Generated by Django 2.2 on 2020-05-02 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='bol_field',
            field=models.BooleanField(default=True),
        ),
    ]
