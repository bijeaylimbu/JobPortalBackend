# Generated by Django 3.2.4 on 2021-06-10 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0025_alter_jobs_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
