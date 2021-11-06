# Generated by Django 3.2.3 on 2021-11-06 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='row',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='bdate',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='bplace',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='mbti',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='profile',
            name='message',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='sns',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='topic_content',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.DeleteModel(
            name='Keyword',
        ),
        migrations.DeleteModel(
            name='Row',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
