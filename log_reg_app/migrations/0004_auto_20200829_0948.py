# Generated by Django 2.2 on 2020-08-29 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg_app', '0003_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='car_pic',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='make',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='model',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='year',
            field=models.CharField(max_length=255, null=True),
        ),
    ]