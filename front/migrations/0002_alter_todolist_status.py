# Generated by Django 4.2.3 on 2023-08-01 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
