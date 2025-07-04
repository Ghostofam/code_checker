# Generated by Django 4.1.13 on 2025-05-03 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0009_assignment_assignmentresponse'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assignmentresponse',
            options={'ordering': ['created_at']},
        ),
        migrations.RenameField(
            model_name='assignmentresponse',
            old_name='submitted_at',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='coding_questions',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='theory_questions',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='total_coding_questions',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='total_theory_questions',
        ),
        migrations.AddField(
            model_name='assignment',
            name='total_questions',
            field=models.IntegerField(default=10, help_text='Should always be 10 (8 coding + 2 theory)'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='score',
            field=models.IntegerField(default=0, help_text='Number of correct answers'),
        ),
    ]
