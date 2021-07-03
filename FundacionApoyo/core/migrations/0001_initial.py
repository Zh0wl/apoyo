# Generated by Django 3.2.3 on 2021-07-03 18:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aportes',
            fields=[
                ('idRegistro', models.IntegerField(primary_key=True, serialize=False)),
                ('rut', models.IntegerField()),
                ('nombre', models.CharField(max_length=255)),
                ('aporte', models.IntegerField()),
                ('fecha', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
