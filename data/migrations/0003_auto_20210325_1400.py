# Generated by Django 3.1.7 on 2021-03-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20210325_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='semester_code',
            field=models.CharField(max_length=200),
        ),
    ]