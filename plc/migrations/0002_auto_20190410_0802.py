# Generated by Django 2.2 on 2019-04-10 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arduino',
            old_name='negative',
            new_name='humidity',
        ),
        migrations.RenameField(
            model_name='arduino',
            old_name='temp',
            new_name='temperature',
        ),
    ]
