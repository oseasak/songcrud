# Generated by Django 4.1.2 on 2022-10-26 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_lyric_song_lyric_content_lyric_song_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lyric',
            old_name='song_id',
            new_name='songs_id',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='Artist_id',
            new_name='artist_id',
        ),
    ]
