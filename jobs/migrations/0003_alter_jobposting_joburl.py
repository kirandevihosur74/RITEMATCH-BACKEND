# Generated by Django 4.1.1 on 2023-11-09 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_remove_jobposting_dateposted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposting',
            name='jobUrl',
            field=models.URLField(),
        ),
    ]