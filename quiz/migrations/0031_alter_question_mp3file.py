# Generated by Django 3.2.4 on 2022-08-03 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0030_question_mp3file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='mp3file',
            field=models.FileField(default=False, upload_to=''),
        ),
    ]
