
from  flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting news
    my_news = get_news()
    return render_template('index.html',news = my_news)

@app.route('/news/<id>')
def article(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    
    return render_template('article.html',id = movie_id)