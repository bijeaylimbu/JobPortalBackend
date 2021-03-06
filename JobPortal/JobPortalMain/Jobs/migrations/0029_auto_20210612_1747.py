# Generated by Django 3.2.4 on 2021-06-12 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0028_jobs_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='post_by',
        ),
        migrations.AlterField(
            model_name='jobs',
            name='before_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='company_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='education',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='experience',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='job_category',
            field=models.CharField(choices=[('IT - Software / Hardware / Networking', 'IT - Software / Hardware / Networking'), ('Business / Administration', 'Business / Administration'), ('Engineering', 'Engineering'), ('Marketing / Sales ', 'Marketing / Sales '), ('Medical / Healthcare', 'Medical / Healthcare'), ('Accounts / Finance', 'Accounts / Finance'), ('Education / Course / Language', 'Education / Course / Language'), ('Other', 'Other')], max_length=255),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='job_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='location',
            field=models.CharField(choices=[('Kathmandu', 'Kathmandu'), ('Pokhara', 'Pokhara'), ('Lalitpur', 'Lalitpur'), ('Bharatpur', 'Bharatpur'), ('Biratnagar', 'Biratnagar'), ('Janakpur', 'Janakpur'), ('Ghorahi', 'Ghorahi'), ('Hetauda', 'Hetauda'), ('Dhangadhi', 'Dhangadhi'), ('Tulsipur', 'Tulsipur'), ('Itahari', 'Itahari'), ('Nepalgunj', 'Nepalgunj'), ('Butwal', 'Butwal'), ('Dharan', 'Dharan'), ('Kalaiya', 'Kalaiya'), ('Jitpursimara', 'Jitpursimara'), ('Other', 'Other')], max_length=255),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='position',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='responsiblities',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='skill',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='what_we_offer',
            field=models.TextField(),
        ),
    ]
