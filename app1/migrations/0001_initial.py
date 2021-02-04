# Generated by Django 3.1.1 on 2021-02-04 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audios_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(blank=True, max_length=254)),
                ('audio_name', models.CharField(default='', max_length=100)),
                ('audio_data', models.FileField(upload_to='files')),
            ],
        ),
        migrations.CreateModel(
            name='TXT_Txt_Speech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(blank=True, max_length=254)),
                ('TXT_File_data', models.FileField(upload_to='files')),
                ('TXT_audio_name', models.CharField(default='', max_length=100)),
                ('TXT_audio_data', models.FileField(upload_to='files')),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]