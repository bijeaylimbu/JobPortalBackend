# Generated by Django 3.2.4 on 2021-06-10 00:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Jobs', '0003_remove_jobs_post_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='Experience',
            new_name='experience',
        ),
        migrations.AddField(
            model_name='jobs',
            name='post_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='position',
            field=models.CharField(default='dsfds', max_length=255),
        ),
    ]
