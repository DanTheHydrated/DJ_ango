from groovy.models import *
from groovy.serializers import *
from rest_framework import status, generics
# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from rest_framework.response import Response
# from django.http.response import Http404
# from rest_framework.views import APIView
# from rest_framework import status


# Create your views here.

class GenresList(generics.ListCreateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer()

class GenresOther(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer()

class ArtistsList(generics.ListCreateAPIView):
    queryset = Artists.objects.all()
    serializer_class = ArtistsSerializer()

class ArtistsOther(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artists.objects.all()
    serializer_class = ArtistsSerializer()

class AlbumsList(generics.ListCreateAPIView):
    queryset = Albums.objects.all()
    serializer_class = AlbumsSerializer()

class AlbumsOther(generics.RetrieveUpdateDestroyAPIView):
    queryset = Albums.objects.all()
    serializer_class = AlbumsSerializer()

class SongsList(generics.ListCreateAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer()

class SongsOther(generics.RetrieveUpdateDestroyAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer()

class PlaylistList(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer()

class PlaylistOther(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer()
# def song_list(request):
#     """
#     list all songs, or Create a Song.
#     """
#     if request.method == 'GET':
#         songs = Songs.objects.all()
#         return JsonResponse(serializer.data, safe = False)
        
#     elif request.method== 'POST':
#         data = JSONParser().parse(request)
        