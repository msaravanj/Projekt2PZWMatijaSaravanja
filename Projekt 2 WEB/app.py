from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_caching import Cache
import requests
from datetime import datetime


app = Flask(__name__)

app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'flatly'
bootstrap = Bootstrap(app)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route("/")

def index():
    return render_template('index.html')


@app.template_filter('datetime')
def fomat_datetime(value, format = '%d.%m.%Y %H:%M'):
    return datetime.fromtimestamp (value).strftime(format)

@app.route('/ekipe') 
def ekipe():
    return render_template('ekipe.html')


@app.route('/kontakt')
@cache.cached(timeout=60)
def kontakt():
    now = datetime.now()
    url = 'http://api.openweathermap.org/data/2.5/weather'
    parameters = {'q': 'Bibinje', 'appid': 'a48ecaafdc2a0c3e78250523c740a66c','lang': 'hr', 'units': 'metric'}
    response = requests.get(url, parameters)
    weather = response.json()
    return render_template('kontakt.html',weather=weather, datetime=datetime, now=now)


@app.errorhandler(404)
def invalid_route(e):
    return render_template('error404.html')    


