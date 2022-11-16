from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=1000)
    songs = models.ForeignKey('Songs', on_delete=models.PROTECT, null=True)
    # albums = models.ForeignKey("Albums", on_delete=models.PROTECT)
    # genre = models.ForeignKey("Genres", on_delete=models.PROTECT)

    def __str__(self):
        return self.Artist


class Songs(models.Model):
    title = models.CharField(max_length=100)
    duration = models.DecimalField(decimal_places=2, max_digits=4)
    # genre = models.ForeignKey("Genres", on_delete=models.PROTECT)


    def __str__(self):
        return self.Songs

class Albums(models.Model):
    cover = models.CharField(max_length=100)
    songs = models.ForeignKey("Songs", on_delete=models.PROTECT)
    # genre = models.ForeignKey("Genres", on_delete=models.PROTECT)

    def __str__(self):
        return self.Albums



