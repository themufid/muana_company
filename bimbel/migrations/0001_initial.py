# Generated by Django 4.1.7 on 2023-09-19 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jadwal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hari', models.CharField(max_length=100)),
                ('jam_pelajaran', models.CharField(max_length=100)),
                ('mata_pelajaran', models.CharField(max_length=100)),
                ('kelas', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JadwalForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hari', models.CharField(max_length=255)),
                ('jam_pelajaran', models.CharField(max_length=255)),
                ('mata_pelajaran', models.CharField(max_length=255)),
                ('kelas', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Presensi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_siswa', models.CharField(max_length=100)),
                ('tanggal', models.DateField()),
                ('hadir', models.BooleanField()),
                ('tutor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Testimoni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('testimoni', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
            ],
        ),
    ]
