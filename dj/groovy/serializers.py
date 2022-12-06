from dj.models import *
from rest_framework import serializers


class  SongsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    duration = serializers.DecimalField(max_digits=4, decimal_places=2)
    genre = serializers.PrimaryKeyRelatedField(many=False, queryset=Genres.objects.all())
    artists = serializers.PrimaryKeyRelatedField(many=True, queryset= Artists.objects.all() )
    album = serializers.PrimaryKeyRelatedField(many=False, queryset= Albums.objects.all() )

    class Meta:
        model = Song 
        field = ['id', 'title', 'duration', 'genre', 'artists', 'album']
        def create(self, validated_data):
            return Song.objects.create(**validated_data)
        def update(self, validated_data, instance):
            instance.title = validated_data.get('title', instance.title)
            instance.artists = validated_data.get('artists', instance.artists)
            instance.duration = validated_data.get('duration', instance.duration)
            instance.genre = validated_data.get('genre', instance.genre)
            instance.album = validated_data.get('album', instance.album)
            instance.save()
            return instance


class ArtistsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    bio = serializer.CharField()

    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio']
    def create(self, validated_data):
        return Artists.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.save()
        return instance


class GenresSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializer.CharField(required=True)

    class Meta:
        model = Genres
        fields = ['id', 'name']
    def create(self, validated_data):
            return Genres.objects.create(**validated_data)
    def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.save()
            return instance 


class AlbumsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializer.CharField(required=True)
    genre = serializer.PrimaryKeyRelatedField(many=False, queryset=Genres.objects.all())
    artists = serializer.PrimaryKeyRelatedField(many=False, queryset=Artists.objects.all())

    class Meta:
        model =  Albums 
        fields = ['id', 'name', 'artists', 'genre']
    def create(self, validated_data):
        return Albums.objects.all(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.artists = validated_data.get('artists', instance.artists)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.save()
        return instance


class PlaylistSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializer.CharField(required=True)

    class Meta:
        model = Playlist
        fields = ['id', 'name']
    def create(elf, validated_data):
        return Playlist.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class SongsInPlaylist(serializers.ModelSerializer):
    playlist = serializers.PrimaryKeyRelatedField(many=False, queryset=Playlist.objects.all())
    songs = serializers.PrimaryKeyRelatedField(many=True, queryset= Songs.objects.all())

    class Meta:
        model = SongsinPLaylist
        fields = ['playlist', 'song']
    def create(self, validated_data):
        return SongsInPlaylist.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.playlist = validated_data.get('playlist', instance.playlist)
        instance.song = validated_data.get('song', instance.song)
        instance.save()
        return instance






# class AlbumSerializer(serializer.ModelSerializer):
#     class meta:
#         model = Album
#         fields = ['album_titles']

# class ArtistsSerializer(serializer.ModelSerializer):
#     albums = AlbumSerializer(source='Albums_id')
#     class meta:
#         model = Artists
#         fields = ['name', 'bio', 'songs', 'albums']

# class GenresSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = genres
#         fields = ['id', 'name']

# class ArtistsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = artists
#         fields = '__all__'

# class UssersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ussers
#         fields = '__all__'

# class SongsSerializer(serializers.ModelSerializer):
#     album = AlbumsSerializer()
#     genre = GenresSerializer()
#     artists = ArtistsSerializer(many = True)
#     class Meta:
#         model = songs
#         fields = ['id', 'title', 'duration', 'album', 'genre', 'artists']

# class AlbumsSerializer(serializers.ModelSerializer):
#     songs = SongsSerializer(many = True)
#     genre = GenresSerializer()
#     artists = ArtistsSerializer()
#     class Meta:
#         model = albums
#         fields = ['id', 'name', 'songs', 'genre', 'artsts']

# class PlaylistSerializer(serializers.ModelSerializer):
#     usser = UssersSerializer()
#     songs = SongsSerializer(many = True)
#     class Meta:
#         model = Playlist
#         fields = ['id', 'name', 'usser', 'songs']