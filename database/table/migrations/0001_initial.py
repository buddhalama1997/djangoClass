# Generated by Django 4.0.3 on 2022-04-21 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField(max_length=70)),
                ('stuname', models.CharField(max_length=70)),
                ('stuemail', models.EmailField(max_length=70)),
            ],
        ),
    ]
