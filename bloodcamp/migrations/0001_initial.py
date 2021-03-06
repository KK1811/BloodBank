# Generated by Django 2.1.2 on 2018-11-16 20:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodCamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campid', models.CharField(max_length=150)),
                ('startdate', models.DateTimeField(blank=True, null=True)),
                ('enddate', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(max_length=150)),
                ('status', models.CharField(default='1', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='BloodCampDonor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=11)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], max_length=15)),
                ('date', models.DateTimeField(default=datetime.date.today)),
                ('blood', models.CharField(choices=[('A+', 'A-'), ('A-', 'A+'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], default='B-', max_length=10)),
                ('bloodcamp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloodcamp.BloodCamp')),
            ],
        ),
        migrations.CreateModel(
            name='BloodVolunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=11)),
                ('state', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Goa', 'Goa'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('karnataka', 'karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Goa', 'Goa'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal')], default='Uttar Pradesh', max_length=30)),
                ('city', models.CharField(default='Agra', max_length=200)),
                ('locality', models.CharField(max_length=400)),
                ('house', models.CharField(max_length=200)),
                ('landmark', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], max_length=15)),
                ('date', models.DateTimeField(default=datetime.date.today)),
                ('blood', models.CharField(choices=[('A+', 'A-'), ('A-', 'A+'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=10)),
                ('bloodcamp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloodcamp.BloodCamp')),
            ],
        ),
    ]
