# Generated by Django 4.2.4 on 2023-09-03 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='title',
            field=models.CharField(default='', max_length=256),
        ),
    ]
