import os
import requests


api_key = os.getenv('TMDB_API_KEY')

def get_movies(query):
    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}'
    
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3OTMxM2FiM2RlM2FiZjhiNzk2YjJlN2U4YTg5MGM2YiIsInN1YiI6IjY2NGE1OGUxNzUwOTY5OGEwMTFkOWJiOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.xwxzT61osz5AmFPf7biNvycx-iwWIbFdb8wi12LeO4I"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return {"error": f"Failed to fetch movies, status code: {response.status_code}"}
    
    movies = response.json().get('results', [])
    result = []
    for movie in movies:
        result.append({
            'id': movie.get('id'),
            'title': movie.get('title'),
            'description': movie.get('overview'),
            'release_date': movie.get('release_date'),
            'rating': movie.get('vote_average'),
            'poster_url': f"https://image.tmdb.org/t/p/w500{movie.get('poster_path')}" if movie.get('poster_path') else None,
            'trailer': f"https://api.themoviedb.org/3/movie/{movie.get}/videos?api_key={api_key}",
        })
    
    return {"results": result}


def get_movie_videos(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={api_key}'
    response = requests.get(url)
    return response.json()

