# Generated by Django 4.0.3 on 2023-10-06 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_more_delete_features'),
    ]

    operations = [
        migrations.AddField(
            model_name='more',
            name='nationality',
            field=models.CharField(default=True, max_length=30),
        ),
        migrations.AddField(
            model_name='more',
            name='phone',
            field=models.CharField(default=True, max_length=30),
        ),
        migrations.AddField(
            model_name='more',
            name='state',
            field=models.CharField(default=True, max_length=30),
        ),
    ]
