# Generated by Django 3.2.4 on 2021-07-02 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_alter_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=200),
        ),
    ]
