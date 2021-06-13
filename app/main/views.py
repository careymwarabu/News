from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_articles,get_sources

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    sources_categories = get_sources('general')
    title="Welcome to the News Article"
    return render_template('index.html', title=title,general=sources_categories)


@main.route('/news/<id>')
def articles(id):

    '''
    View news page function that returns the news details page and its data
    '''

    article_items=get_article(id)
    title = f'{id}'
    return render_template('news.html',title = title,articles=article_items)