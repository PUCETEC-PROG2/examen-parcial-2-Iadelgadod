from django.urls import path
from .views import movie_list
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:movie_id>/", views.movie_list, name="movie_list"),
]
