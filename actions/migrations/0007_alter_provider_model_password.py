# Generated by Django 4.2 on 2024-02-16 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0006_provider_model_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider_model',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
