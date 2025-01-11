
from django.shortcuts import HttpResponse
from django.template import loader
from .models import Movie
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'movies': movies,
    }, request))
    
    
def movie_list(request, movie_id):
    movie_list = Movie.objects.get(pk = movie_id)
    template = loader.get_template('movie_list.html')
    context = {
        'movie': movie_list
    }
    return HttpResponse(template.render(context, request))
    
