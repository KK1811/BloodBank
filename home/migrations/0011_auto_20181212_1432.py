# Generated by Django 2.1.2 on 2018-12-12 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20181212_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='landmark',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
