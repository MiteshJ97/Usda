# Generated by Django 4.2 on 2024-02-22 15:38

import actions.archive_article
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archived_article_attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.URLField()),
                ('file_name', models.FileField(blank=True, null=True, storage=actions.archive_article.OverWriteStorage(), upload_to=actions.archive_article.get_file_path)),
                ('received_on', models.DateTimeField(auto_now_add=True)),
                ('processed_on', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('waiting', 'waiting'), ('processed', 'processed'), ('failed', 'failed')], max_length=12)),
                ('notes', models.TextField(default='N/A')),
            ],
        ),
        migrations.CreateModel(
            name='Provider_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('official_name', models.CharField(max_length=100)),
                ('working_name', models.CharField(max_length=50)),
                ('delivery_method', models.CharField(max_length=50)),
                ('source_schema', models.CharField(max_length=50)),
                ('minimum_delivery_fq', models.IntegerField()),
                ('in_production', models.BooleanField(max_length=15)),
                ('archive_switch', models.BooleanField(max_length=15)),
                ('article_switch', models.BooleanField(max_length=15)),
                ('requirement_override', models.BooleanField(max_length=15)),
                ('deposit_path', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Provider_meta_data_FTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server', models.TextField()),
                ('protocol', models.CharField(max_length=10)),
                ('site_path', models.CharField(max_length=50)),
                ('account', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('last_pull_time', models.DateTimeField(auto_now=True)),
                ('pull_switch', models.BooleanField()),
                ('last_pull_status', models.CharField(default='pass', max_length=10)),
                ('next_due_date', models.DateTimeField(null=True)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ftp_provider', to='actions.provider_model')),
            ],
        ),
        migrations.CreateModel(
            name='Provider_meta_data_API',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_url', models.URLField()),
                ('identifier_code', models.CharField(max_length=50)),
                ('identifier_type', models.CharField(max_length=50)),
                ('last_pull_time', models.DateTimeField(auto_now=True)),
                ('api_switch', models.BooleanField()),
                ('site_token', models.TextField()),
                ('last_pull_status', models.CharField(default='pass', max_length=10)),
                ('next_due_date', models.DateTimeField(null=True)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='api_provider', to='actions.provider_model')),
            ],
        ),
    ]
