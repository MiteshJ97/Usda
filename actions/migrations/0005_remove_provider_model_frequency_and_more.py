# Generated by Django 4.2 on 2024-02-16 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0004_provider_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provider_model',
            name='frequency',
        ),
        migrations.RemoveField(
            model_name='provider_model',
            name='host_name',
        ),
        migrations.RemoveField(
            model_name='provider_model',
            name='last_accessed_at',
        ),
        migrations.RemoveField(
            model_name='provider_model',
            name='last_status',
        ),
        migrations.RemoveField(
            model_name='provider_model',
            name='next_due_date',
        ),
        migrations.RemoveField(
            model_name='provider_model',
            name='pass_code',
        ),
        migrations.RemoveField(
            model_name='provider_model',
            name='provider_address',
        ),
        migrations.RemoveField(
            model_name='provider_model',
            name='provider_name',
        ),
        migrations.RemoveField(
            model_name='provider_model',
            name='user_id',
        ),
        migrations.AddField(
            model_name='provider_model',
            name='archive_switch',
            field=models.BooleanField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provider_model',
            name='article_switch',
            field=models.BooleanField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provider_model',
            name='delivery_method',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provider_model',
            name='deposit_path',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provider_model',
            name='email',
            field=models.EmailField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provider_model',
            name='in_production',
            field=models.BooleanField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provider_model',
            name='minimum_delivery_fq',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provider_model',
            name='official_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provider_model',
            name='requirement_override',
            field=models.BooleanField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provider_model',
            name='source_schema',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provider_model',
            name='working_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
