# Generated by Django 4.2.3 on 2023-08-04 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courselist', '0007_alter_courselist_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courselist',
            name='icon',
            field=models.CharField(choices=[('python', 'python'), ('javascript', 'javascript'), ('c', 'c'), ('css', 'css'), ('java', 'java'), ('swift', 'swift'), ('scala', 'scala'), ('kotlin', 'kotlin'), ('php', 'php'), ('ruby', 'ruby'), ('rust', 'rust'), ('html', 'html'), ('default', 'default')], default='default', max_length=20),
        ),
    ]