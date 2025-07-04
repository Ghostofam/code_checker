# Generated by Django 4.1.13 on 2025-04-15 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0004_userprogress_accuracy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubmission',
            name='time_taken',
            field=models.FloatField(default=0.0, help_text='Time taken to solve the question in seconds'),
        ),
        migrations.CreateModel(
            name='TheoryQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expertise_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.expertiselevel')),
                ('programming_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.programminglanguage')),
            ],
        ),
        migrations.CreateModel(
            name='MCQQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('options', models.JSONField()),
                ('correct_option', models.CharField(max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expertise_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.expertiselevel')),
                ('programming_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.programminglanguage')),
            ],
        ),
    ]
