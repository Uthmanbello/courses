# Generated by Django 4.2.3 on 2023-07-30 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courselist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courselist',
            name='icon',
            field=models.CharField(choices=[('icon1', 'Icon 1'), ('icon2', 'Icon 2'), ('icon3', 'Icon 3')], default='default_icon', max_length=20),
        ),
    ]
