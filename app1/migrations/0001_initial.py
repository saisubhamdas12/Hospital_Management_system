# Generated by Django 4.2.5 on 2023-11-05 06:16

import app1.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('Doctor_id', models.CharField(default=app1.models.generate_short_uuid, max_length=5, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Famale', 'Famale')], default='Male', max_length=50)),
                ('Profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/PatientProfilePic/')),
                ('Address', models.CharField(max_length=40)),
                ('Mobile', models.CharField(max_length=20, null=True)),
                ('Department', models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists')], default='Cardiologist', max_length=50)),
                ('Status', models.BooleanField(default=True)),
                ('Document', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('Patient_id', models.CharField(default=app1.models.generate_short_uuid, max_length=6, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Famale', 'Famale')], default='Male', max_length=50)),
                ('Profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/PatientProfilePic/')),
                ('Address', models.CharField(max_length=40)),
                ('Mobile', models.CharField(max_length=20, null=True)),
                ('Status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/PatientProfilePic/')),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Famale', 'Famale')], default='Male', max_length=50)),
                ('Address', models.CharField(max_length=40)),
                ('Mobile', models.CharField(max_length=20, null=True)),
                ('Status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prescriptins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emailaddress', models.EmailField(max_length=254)),
                ('PatientGender', models.CharField(max_length=50)),
                ('Prescriptins', models.TextField()),
                ('Doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.doctor')),
                ('Patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientName', models.CharField(max_length=40, null=True)),
                ('DoctorName', models.CharField(max_length=40, null=True)),
                ('PatientGender', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('Phoneno', models.CharField(max_length=10)),
                ('Emailaddress', models.EmailField(max_length=254)),
                ('Neurological', models.CharField(default='no', max_length=100)),
                ('Pychological', models.CharField(default='no', max_length=100)),
                ('Other', models.CharField(default='no', max_length=100)),
                ('Diagnosis', models.TextField()),
                ('Doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.doctor')),
                ('Patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientName', models.CharField(max_length=40, null=True)),
                ('DoctorName', models.CharField(max_length=40, null=True)),
                ('Emailaddress', models.EmailField(max_length=254)),
                ('Gender', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Patientmobile', models.CharField(max_length=20, null=True)),
                ('AppointmentDate', models.DateField(auto_now=True)),
                ('Symptoms', models.CharField(max_length=100, null=True)),
                ('Description', models.TextField(max_length=500)),
                ('Doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.doctor')),
                ('Patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientName', models.CharField(max_length=40, null=True)),
                ('Emailaddress', models.EmailField(max_length=254)),
                ('Gender', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=100)),
                ('Date', models.DateField(auto_now=True)),
                ('Time', models.TimeField()),
                ('Patientmobile', models.CharField(max_length=20, null=True)),
                ('AppointmentDate', models.DateField()),
                ('Symptoms', models.CharField(max_length=100, null=True)),
                ('Description', models.TextField(max_length=500)),
                ('Doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.doctor')),
                ('Patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.patient')),
            ],
        ),
    ]