# Generated by Django 3.0.3 on 2020-02-23 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('week2_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
