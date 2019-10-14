
from  flask import render_template
from . import main
from ..request import get_news,get_article

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting news
    my_news = get_news()
    return render_template('index.html',news = my_news)

@main.route('/articles/<id>')
def article(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    
    my_articles = get_article(id)
    return render_template('article.html', artic = my_articles)