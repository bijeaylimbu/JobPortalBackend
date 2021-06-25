# Generated by Django 3.2.4 on 2021-06-10 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0010_auto_20210610_0008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobs',
            options={'ordering': ['post_date']},
        ),
        migrations.AddField(
            model_name='jobs',
            name='before_date',
            field=models.DateField(default='2020-10-2'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='education',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='jobs',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='jobs',
            name='experience',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='jobs',
            name='job_category',
            field=models.CharField(blank=True, choices=[('IT - Software / Hardware / Networking', 'IT - Software / Hardware / Networking'), ('Business / Administration', 'Business / Administration'), ('Engineering', 'Engineering'), ('Marketing / Sales ', 'Marketing / Sales '), ('Medical / Healthcare', 'Medical / Healthcare'), ('Accounts / Finance', 'Accounts / Finance'), ('Education / Course / Language', 'Education / Course / Language'), ('Other', 'Other')], max_length=255),
        ),
        migrations.AddField(
            model_name='jobs',
            name='job_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='position',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='jobs',
            name='post_date',
            field=models.DateField(default='2020-2-2'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='responsiblities',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='skill',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='what_we_offer',
            field=models.TextField(blank=True),
        ),
    ]