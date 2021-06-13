
import urllib.request
import json
from .models import Sources, Headlines


# Getting api key
api_key = None

# Getting the base urls
base_url = None
headline_base_url = None



def configure_request(app):
    global api_key,base_url,headline_base_url

    api_key=app.config['API_KEY']
    base_url = app.config['SOURCE_BASE_URL']
    headline_base_url=app.config['HEADLINES_BASE_URL']



def get_sources(category):
    '''
    a function that returns sources with category passed in as a parameter
    '''
    full_url = base_url.format(category,api_key)
    with urllib.request.urlopen(full_url) as url:
        source_data = url.read()
        json_source_data = json.loads(source_data)
        # print(json_source_data)

        source_list = None

        if json_source_data['sources']:
            json_lib = json_source_data['sources']
            source_list = process_sources(json_lib)

    return source_list


def process_sources(sources):
    '''
    an 'interface' that filters data and inserts it into a class
    '''
    source_list = []
    for one_source in sources:
        id = one_source.get('id')
        name = one_source.get('name')
        desc = one_source.get('description')
        url = one_source.get('url')
        country = one_source.get('country')
       

        data_sources = Sources(id,name,desc,url,country)
        source_list.append(data_sources)
        # print('full_headlines_url')

    return source_list


def get_articles(id):
    '''
    a function that returns article_list irrespective of their category
    '''
    print('full_headlines_url')
    full_headlines_url = headline_base_url.format(id, api_key)

    with urllib.request.urlopen(full_headlines_url) as url:
        articles = url.read()
        json_articles = json.loads(articles)
        print(json_articles)

        articles_list = None

        if json_articles['articles']:
            article_lib = json_articles['articles']
            articles_list = process_articles(article_lib)

    return articles_list


def process_articles(articles):
    '''
    this function acr=ts an an interfacce for data brought back by the api url as it pushes relevant data into our class and irrellevant data is left out
    '''
    articles_list = []
    for article in articles:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')

        article_data = Headlines(
            author, title, description, url, urlToImage, publishedAt)

        articles_list.append(article_data)

    return articles_list