from django.shortcuts import render, redirect
from .models import Emenitites, Movie
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import logout
# import json

# with open('book\movies.json') as json_file:
#     data = json.load(json_file)


# movies_data = {}
# for i in data:
#     movies_data['Title'] = i['movies'][0]['title']
#     movies_data['Poster'] = i['movies'][0]['poster']
#     movies_data['Genres'] = i['movies'][0]['genre']
#     movies_data['Rating'] = i['movies'][0]['imdb_rating']
#     movies_data['Year Release'] = i['movies'][0]['year'] 
#     movies_data['Metacritic Rating'] = i['movies'][0]['meta_score']
#     movies_data['Runtime'] = i['movies'][0]['runtime']
    

def home(request): 

    movies_data = [{'Title': 'In the Mood for Love', 'Poster': 'https://m.media-amazon.com/images/M/MV5BYjZjODRlMjQtMjJlYy00ZDBjLTkyYTQtZGQxZTk5NzJhYmNmXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg', 'Genres': ['Drama', 'Romance'], 'Rating': '8.1', 'YearRelease': '2000', 'MetacriticRating': '85', 'Runtime': '98 min'}, {'Title': 'The Love Witch', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMjA5NDEyMjQwNV5BMl5BanBnXkFtZTgwNDQ1MjMwMDI@._V1_SX300.jpg', 'Genres': ['Romance', 'Thriller'], 'Rating': '6.2', 'YearRelease': '2016', 'MetacriticRating': '82', 'Runtime': '120 min'}, {'Title': 'Persepolis', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMGRkZThmYzEtYjQxZC00OWEzLThjYjAtYzFkMjY0NGZkZWI4XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SX300.jpg', 'Genres': ['Animation', 'Biography', 'Drama', 'History', 'War'], 'Rating': '8.1', 'YearRelease': '2007', 'MetacriticRating': '90', 'Runtime': '96 min'}, {'Title': 'Jumanji: Welcome to the Jungle', 'Poster': 'https://m.media-amazon.com/images/M/MV5BODQ0NDhjYWItYTMxZi00NTk2LWIzNDEtOWZiYWYxZjc2MTgxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg', 'Genres': ['Action', 'Adventure', 'Comedy', 'Fantasy'], 'Rating': '7.0', 'YearRelease': '2017', 'MetacriticRating': '58', 'Runtime': '119 min'}, {'Title': 'Pariah', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMTM1MTQyNTY3NV5BMl5BanBnXkFtZTcwODk0ODk2Ng@@._V1_SX300.jpg', 'Genres': ['Drama'], 'Rating': '7.2', 'YearRelease': '2011', 'MetacriticRating': '79', 'Runtime': '86 min'}, {'Title': 'Human Traffic', 'Poster': 'https://m.media-amazon.com/images/M/MV5BM2ZlMjIxZjgtZGJiMC00ODAwLWJhNWYtYWJkZDg2Y2VkM2QyXkEyXkFqcGdeQXVyMjA0MzYwMDY@._V1_SX300.jpg', 'Genres': ['Comedy', 'Music'], 'Rating': '7.1', 'YearRelease': '1999', 'MetacriticRating': '53', 'Runtime': '99 min'}, {'Title': 'A Most Violent Year', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMjE4OTY4ODg3Ml5BMl5BanBnXkFtZTgwMTI1MTg1MzE@._V1_SX300.jpg', 'Genres': ['Crime', 'Drama', 'Thriller'], 'Rating': '7.0', 'YearRelease': '2014', 'MetacriticRating': '79', 'Runtime': '125 min'}, {'Title': 'Seconds', 'Poster': 'https://m.media-amazon.com/images/M/MV5BYmYwMmFjMDYtYTEyYS00NzUwLWIyZTMtNjFjZmVmZjhkY2M1XkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_SX300.jpg', 'Genres': ['Sci-Fi', 'Thriller'], 'Rating': '7.7', 'YearRelease': '1966', 'MetacriticRating': 'N/A', 'Runtime': '106 min'}, {'Title': 'Walking Tall', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMTM0MjYzNzM1N15BMl5BanBnXkFtZTcwMDcwNDc3NA@@._V1_SX300.jpg', 'Genres': ['Action', 'Crime'], 'Rating': '6.3', 'YearRelease': '2004', 'MetacriticRating': '44', 'Runtime': '86 min'}, {'Title': 'Isle of Dogs', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMTYyOTUwNjAxM15BMl5BanBnXkFtZTgwODcyMzE0NDM@._V1_SX300.jpg', 'Genres': ['Animation', 'Adventure', 'Comedy', 'Drama', 'Fantasy', 'Sci-Fi'], 'Rating': '7.9', 'YearRelease': '2018', 'MetacriticRating': '82', 'Runtime': '101 min'}]

    return render(request, 'base.html', {'movies_data': movies_data}) 
 
# def api_movies(request):
#     movies_objs = Movie.objects.all()
     
#     price = request.GET.get('price')
#     if price:
#         movies_objs = movies_objs.filter(price__lte=price)
         
#     emenities = request.GET.get('emenities')
#     if emenities:
#         emenities = [int(e) for e in emenities.split(',') if e.isdigit()]
#         movies_objs = movies_objs.filter(emenities__in=emenities).distinct()
     
#     payload = [{'movie_name': movie_obj.movie_name,
#                 'movie_description': movie_obj.movie_description,
#                 'movie_image': movie_obj.movie_image,
#                 'price': movie_obj.price} for movie_obj in movies_objs]
     
#     return JsonResponse(payload, safe=False)
 