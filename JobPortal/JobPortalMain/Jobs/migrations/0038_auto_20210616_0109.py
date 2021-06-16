# Generated by Django 3.2.4 on 2021-06-16 01:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0037_alter_jobs_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='post_date',
            field=models.DateField(default=datetime.date.today, editable=False),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='what_we_offer',
            field=models.TextField(blank=True),
        ),
    ]
