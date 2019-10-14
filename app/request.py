
import  urllib.request,json
from .models import News,Article



# Getting api key
api_key = None
#Getting base url
base_url = None
#Getting article base url
article_base_url = None

def configure_request(app):
    global api_key,base_url,article_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_base_url = app.config['ARTICLE_API_BASE_URL']

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')
        id = news_item.get('id')

           
        if name:
            news_object = News(name,description,url,category,language,country,id)
            news_results.append(news_object)

    return news_results

def get_article(id):
    
    '''
    Function that gets the json response to our url request
    '''
    
    get_article_url = article_base_url.format(id,api_key)
    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)
        
        # article_results = None
        
        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_result(article_results_list)
            
    return article_results
            
def process_result(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    '''    
    
    article_results = []
    
    for article_items in article_list:
        image = article_items.get("urlToImage")
        description = article_items.get('description')
        time = article_items.get('publishedAt')
        author = article_items.get('author')
        site = article_items.get('url')
        
        if image:
            article_object = Article(image,description,time,author,site)
            article_results.append(article_object)
            
            
    return article_results
        
    
    
    
    