# Generated by Django 3.0.8 on 2023-12-11 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other_profile', '0004_alter_report_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
