# Generated by Django 2.2 on 2020-05-02 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0003_auto_20200502_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='bol_field',
        ),
    ]
