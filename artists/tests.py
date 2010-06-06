"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from artist.models import Artist, Song
from django.db.utils import DatabaseError

class ArtistTestCase(TestCase):
    def setUp(self):
        self.zeppelin = Artist.objects.create(name="Led Zeppelin")

    def test_created(self):
        self.assertEquals(self.zeppelin.name, "Led Zeppelin")
        self.assertTrue(self.zeppelin.id > 0)

    def test_add_songs(self):
        name = "Over the Hills and Far Away"
        song = self.zeppelin.addSong(name=name)
        self.assertEquals(song.name, name)
        self.assertTrue(song.id > 0)
        self.assertEquals(len(self.zeppelin.song_ids), 1)

        print(self.zeppelin.songs())

        self.assertEquals(len(self.zeppelin.songs()), 1)

class SongTestCase(TestCase):
    def setUp(self):
        self.modest_mouse = Artist.objects.create(name="Modest Mouse")

    def test_create_song(self):
        mm = Song.objects.create(name="Little Motel", artist_id=self.modest_mouse.id)
        self.assertTrue(mm)

    def test_create_song_Fail(self):
        try:
            Song.objects.create(name="Interstate 8")
        except DatabaseError:
            pass
        else:
            self.fail("Should have thrown a DatabaseError")