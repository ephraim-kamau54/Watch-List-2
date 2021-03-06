# from flask.templating import render_template


from flask import app, render_template,request,redirect,url_for
from . import main
from ..requests import get_movies,get_movie,search_movie
from .forms import ReviewForm
from .models import Review

# # Views
# @app.route('/movie/<int:movie_id>')
# def movie(movie_id):

#     '''
#     View movie page function that returns the movie details page and its data
#     '''
#     return render_template('movie.html',id = movie_id)

from .request import get_movies,get_movie,search_movie

# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''

#     # Getting popular movie
#     popular_movies = get_movies('popular')
#     print(popular_movies)
#     title = 'Home - Welcome to The best Movie Review Website Online'
#     return render_template('index.html', title = title,popular = popular_movies)

# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''

#     # Getting popular movie
#     popular_movies = get_movies('popular')
#     upcoming_movie = get_movies('upcoming')
#     now_showing_movie = get_movies('now_playing')
#     title = 'Home - Welcome to The best Movie Review Website Online'
#     return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )

@app.route('/search/<movie_name>')
def search(movie_name):

    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html',movies = searched_movies)

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')

    title = 'Home - Welcome to The best Movie Review Website Online'

    search_movie = request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('search',movie_name=search_movie))
    else:
        return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )