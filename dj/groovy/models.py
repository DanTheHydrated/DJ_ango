from django.db import models

# Create your models here.
class Genres(models.Model):
    name = models.CharField(max_length=50, null= False)
    class Meta:
        ordering = ['id']
#     # def __str__(self):
#     #     return self.Genres

class Artists(models.Model):
    name = models.CharField(max_length=50, null=False)
    bio = models.CharField(max_length=200, null=False)
    class Meta:
        ordering = ['id']
    # def __str__(self):
    #     return self.Artists

class Albums(models.Model):
    name = models.CharField(max_length= 100)
    artists = models.ForeignKey('Artists', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genres', on_delete=models.CASCADE)
    # songs = models.ForeignKey('Songs', on_delete=models.CASCADE)
    class Meta:
        ordering = ['id']
#     # def __str__(self):
#     #     return self.Albums

class Songs(models.Model):
    title = models.CharField(max_length=100, null=False)
    duration = models.DecimalField(decimal_places=2, max_digits=4, null=False)
    album = models.ForeignKey('Albums', on_delete= models.CASCADE)
    genre = models.ForeignKey('Genres', on_delete=models.CASCADE)
    artist = models.ForeignKey('Artists', on_delete=models.CASCADE)
    class Meta:
        ordering = ['id']
#     # def __str__(self):
#     #     return self.Song

class Playlist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    class Meta:
        ordering = ['id']
#     # def __str__(self):
#     #     return self.Playlist

class SongsInPlaylist(models.Model):
    playlist = models.ForeignKey("Playlist", on_delete=models.CASCADE)
    songs = models.ForeignKey("Songs", on_delete=models.CASCADE)
    class Meta:
        ordering = ['id']
#     # def __str__(self):
#     #     return self.Usser