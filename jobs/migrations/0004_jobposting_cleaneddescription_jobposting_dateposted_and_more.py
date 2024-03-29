# Generated by Django 4.2.5 on 2023-12-11 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_jobposting_joburl'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='cleanedDescription',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='datePosted',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='interval',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='jobposting',
            name='jobType',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
