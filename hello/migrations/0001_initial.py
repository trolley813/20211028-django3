# Generated by Django 3.2.8 on 2021-11-11 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=128)),
                ('floor_count', models.IntegerField()),
                ('build_date', models.DateField()),
            ],
        ),
    ]
