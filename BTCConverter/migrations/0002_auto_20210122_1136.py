# Generated by Django 3.1.4 on 2021-01-22 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BTCConverter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='firstName',
            field=models.CharField(default='x', max_length=40),
        ),
        migrations.AddField(
            model_name='signup',
            name='lastName',
            field=models.CharField(default='x', max_length=40),
        ),
    ]