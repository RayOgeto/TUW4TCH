from django.shortcuts import render
from django.http import JsonResponse
from .tmdb_api import api_key
from .models import Movie
from .tmdb_api import get_movies
from .tmdb_api import get_movie_videos

import requests

# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, '', {'movies': movies})

def search_results(request):
    if 'movie_name' in request.GET:
        movie_name = request.GET['movie_name']
        url = 'https://api.themoviedb.org/3/search/movie'


        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()['results']


            poster_urls = [movie['poster_path'] for movie in data if movie.get('poster_path')]
            # Update movie data with poster URLs
            for i, movie in enumerate(data):
                if movie.get('poster_path'):
                    data[i]['poster_url'] = f'https://image.tmdb.org/t/p/w500{movie["poster_path"]}'
                    data[i]['overview'] = movie.get('overview', 'No overview available')
                    movie_id = movie.get('id')
                if movie_id:
                    movie_details_url = f'https://api.themoviedb.org/3/movie/{movie_id}'
                    details_response = requests.get(movie_details_url, params={'api_key': api_key})
                    if details_response.status_code == 200:
                        details_data = details_response.json()
                        data[i]['movie_rating'] = details_data.get('vote_average', 'No rating available')
                    else:
                        data[i]['movie_rating'] = 'No rating available'
                else:
                    data[i]['movie_rating'] = 'No rating available'
        
        else:
            data = [] 
        
        return render(request,{'data': data, 'query': movie_name})

def search_movies(request):
    query = request.GET.get('query', '')
    if not query:
        return JsonResponse({"error": "Query parameter is missing"}, status=400)
    

    data = get_movies(query)
    return JsonResponse(data)

def movie_details(request, movie_id):
    movie_data = get_movies(movie_id)  # Fetch movie details
    video_data = get_movie_videos(movie_id)  # Fetch movie videos
    movie_data['videos'] = video_data.get('results', [])
    return JsonResponse(movie_data)

