# Generated by Django 4.2.17 on 2025-04-08 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
