# Generated by Django 4.0.3 on 2022-04-21 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stuid',
            field=models.IntegerField(),
        ),
    ]
