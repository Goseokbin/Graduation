# Generated by Django 2.2 on 2019-10-26 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plc', '0003_auto_20191014_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Set_Outlier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_max', models.IntegerField()),
                ('h_min', models.IntegerField()),
                ('t_max', models.IntegerField()),
                ('t_min', models.IntegerField()),
                ('e_max', models.IntegerField()),
                ('e_min', models.IntegerField()),
                ('i_max', models.IntegerField()),
                ('i_min', models.IntegerField()),
            ],
        ),
    ]
