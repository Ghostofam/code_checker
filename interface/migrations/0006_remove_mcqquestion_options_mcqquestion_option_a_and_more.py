# Generated by Django 4.1.13 on 2025-04-16 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0005_usersubmission_time_taken_theoryquestion_mcqquestion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mcqquestion',
            name='options',
        ),
        migrations.AddField(
            model_name='mcqquestion',
            name='option_a',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mcqquestion',
            name='option_b',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mcqquestion',
            name='option_c',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mcqquestion',
            name='option_d',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
