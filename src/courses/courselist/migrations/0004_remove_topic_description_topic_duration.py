# Generated by Django 4.2.3 on 2023-08-01 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courselist', '0003_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='description',
        ),
        migrations.AddField(
            model_name='topic',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]
