# Generated by Django 3.2b1 on 2021-03-16 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0004_alter_playlist_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='videos',
        ),
    ]
