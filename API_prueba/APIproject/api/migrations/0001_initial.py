# Generated by Django 3.2.7 on 2021-09-17 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIad',
            fields=[
                ('legajo', models.IntegerField()),
                ('id_ad', models.IntegerField(primary_key=True, serialize=False)),
                ('desc_larga', models.CharField(max_length=100)),
                ('importe', models.FloatField()),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
    ]
