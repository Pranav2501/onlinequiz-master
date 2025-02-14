# Generated by Django 3.2.4 on 2021-07-04 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0016_auto_20210704_1112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='email',
            new_name='email_qs',
        ),
        migrations.RenameField(
            model_name='passage',
            old_name='passage',
            new_name='passage_qs',
        ),
        migrations.AddField(
            model_name='question',
            name='email',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.email'),
        ),
        migrations.AddField(
            model_name='question',
            name='passage',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.passage'),
        ),
    ]
