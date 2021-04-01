# Generated by Django 3.1.7 on 2021-03-20 04:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0076_auto_20210320_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amazon',
            name='description',
        ),
        migrations.AddField(
            model_name='amazon',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='amazon',
            name='dateint',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='amazon',
            name='day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=20),
        ),
        migrations.AddField(
            model_name='amazon',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='amazon',
            name='month',
            field=models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], default='January', max_length=20),
        ),
        migrations.AddField(
            model_name='amazon',
            name='now',
            field=models.TimeField(default='09:32:02'),
        ),
        migrations.AddField(
            model_name='amazon',
            name='para4',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='amazon',
            name='para5',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='amazon',
            name='para6',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='amazon',
            name='para7',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='amazon',
            name='subtitle',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='amazon',
            name='youtubevideo',
            field=models.CharField(default='null', max_length=300),
        ),
        migrations.AlterField(
            model_name='amazon',
            name='para1',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AlterField(
            model_name='amazon',
            name='para2',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AlterField(
            model_name='amazon',
            name='para3',
            field=models.CharField(default='', max_length=3000),
        ),
        migrations.AlterField(
            model_name='hot',
            name='now',
            field=models.TimeField(default='09:32:02'),
        ),
        migrations.AlterField(
            model_name='new',
            name='name',
            field=models.CharField(default='new', max_length=120),
        ),
        migrations.AlterField(
            model_name='new',
            name='now',
            field=models.TimeField(default='09:32:02'),
        ),
        migrations.AlterField(
            model_name='trending',
            name='now',
            field=models.TimeField(default='09:32:02'),
        ),
    ]
