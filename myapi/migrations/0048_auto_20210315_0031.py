# Generated by Django 3.1.7 on 2021-03-14 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0047_auto_20210314_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headphones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='headphones', max_length=120)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title', models.CharField(default='', max_length=120)),
                ('description', models.CharField(default='', max_length=5000)),
                ('para1', models.CharField(default='', max_length=200)),
                ('para2', models.CharField(default='', max_length=800)),
                ('para3', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Speakers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='speakers', max_length=120)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title', models.CharField(default='', max_length=120)),
                ('description', models.CharField(default='', max_length=5000)),
                ('para1', models.CharField(default='', max_length=200)),
                ('para2', models.CharField(default='', max_length=800)),
                ('para3', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='trending',
            name='now',
            field=models.TimeField(default='00:31:02'),
        ),
    ]