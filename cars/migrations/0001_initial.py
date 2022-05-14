# Generated by Django 3.2.13 on 2022-05-11 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('car_plate', models.CharField(max_length=50)),
                ('car_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
                'ordering': ('car_name',),
            },
        ),
    ]
