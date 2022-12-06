from django.urls import path
from groovy import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('Genres/', views.Genreslist.as_views())
    # path('Genres/', )
]