# Generated by Django 3.2.4 on 2021-06-14 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0034_auto_20210614_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Contract', 'Contract')], max_length=255),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='number_of_vacancy',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='position_type',
            field=models.CharField(choices=[('Entry Level', 'Entry Level'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')], max_length=255),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='salary',
            field=models.CharField(max_length=255),
        ),
    ]
