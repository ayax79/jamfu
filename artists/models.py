from django.db import models
from djangotoolbox.fields import ListField

class Song(models.Model):
    name = models.CharField(max_length=100)
    artist_id = models.IntegerField(null=False)
    data = models.FileField(upload_to="foo")

    def __unicode__(self):
        return self.name

    def artist(self):
        return Artist.objects.get(self.artist_id)


class Artist(models.Model):
    name = models.CharField(max_length=100)
    song_ids = ListField(models.IntegerField(null=False))

    def __unicode__(self):
        return self.name

    def songs(self):
        after = [] # some cleanup
        songs = []

        for s in self.song_ids:
            try:
                print(s)
                songs.append(Song.objects.get(pk = s))
                after.append(s)
            except Song.DoesNotExist:
                pass

        # perform a little cleanup in case there are bad values
        if (len(after) < len(songs)):
            self.song_ids = after
            self.save()
        return songs


    def add_song(self, **kwArgs):
        kwArgs['artist_id'] = self.id
        s = Song.objects.create(**kwArgs)
        self.song_ids.append(s.id)
        self.save()
        return s
