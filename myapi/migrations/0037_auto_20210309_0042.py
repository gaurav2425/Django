# Generated by Django 3.1.7 on 2021-03-08 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0036_auto_20210308_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='trending',
            name='now',
            field=models.TimeField(default='00:42:35'),
        ),
    ]
