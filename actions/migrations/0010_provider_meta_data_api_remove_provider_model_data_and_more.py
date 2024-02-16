# Generated by Django 4.2 on 2024-02-16 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0009_provider_model_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider_meta_data_API',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_url', models.URLField()),
                ('indentifier_code', models.CharField(max_length=50)),
                ('indentifier_type', models.CharField(max_length=50)),
                ('last_pull_time', models.DateTimeField(auto_now=True)),
                ('api_switch', models.BooleanField()),
                ('site_token', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='provider_model',
            name='data',
        ),
        migrations.RemoveField(
            model_name='provider_model',
            name='email',
        ),
        migrations.RemoveField(
            model_name='provider_model',
            name='password',
        ),
        migrations.CreateModel(
            name='Provider_meta_data_FTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server', models.URLField()),
                ('protocol', models.CharField(max_length=10)),
                ('site_path', models.CharField(max_length=50)),
                ('account', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('last_pull_time', models.DateTimeField(auto_now=True)),
                ('pull_switch', models.BooleanField()),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider', to='actions.provider_model')),
            ],
        ),
    ]
