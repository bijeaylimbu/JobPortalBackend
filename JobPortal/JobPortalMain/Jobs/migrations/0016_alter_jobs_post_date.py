# Generated by Django 3.2.4 on 2021-06-10 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0015_auto_20210610_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='post_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
