from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_articles,get_sources

# Views
@main.route('/')
def index():
    title = 'Home - Welcome to News Article'
    sports = get_sources('sports')
    business = get_sources('business')
    entertainment = get_sources('entertainment')
    general = get_sources('general')
    health = get_sources('health')
    science = get_sources('science')
    technology = get_sources('technology')
    
    return render_template('index.html', title=title, sports=sports,business=business,
                           technology=technology,entertainment=entertainment,
                           general=general,health=health,science=science,)


@main.route('/news/<id>')
def articles(id):

    articles_display = get_articles(id)
    title=f'{id}'
    return render_template('news.html',articles=articles_display,)