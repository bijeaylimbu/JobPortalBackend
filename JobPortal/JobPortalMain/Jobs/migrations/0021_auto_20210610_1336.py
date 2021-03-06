# Generated by Django 3.2.4 on 2021-06-10 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Jobs', '0020_auto_20210610_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='before_date',
            field=models.DateTimeField(default='2020-2-2'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='education',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='experience',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='job_category',
            field=models.CharField(choices=[('IT - Software / Hardware / Networking', 'IT - Software / Hardware / Networking'), ('Business / Administration', 'Business / Administration'), ('Engineering', 'Engineering'), ('Marketing / Sales ', 'Marketing / Sales '), ('Medical / Healthcare', 'Medical / Healthcare'), ('Accounts / Finance', 'Accounts / Finance'), ('Education / Course / Language', 'Education / Course / Language'), ('Other', 'Other')], default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='job_description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='position',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='post_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='post_date',
            field=models.DateTimeField(default='2020-2-2'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='responsiblities',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='skill',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='what_we_offer',
            field=models.TextField(default=''),
        ),
    ]
