from flask import Flask, render_template, request, redirect, url_for
from utils import scrape_health_news, scrape_covid_information
from typing import List, Dict
import os

app: Flask = Flask(__name__, template_folder='templates')

# font awesome code
fa_code = os.environ['fa-code']

# Makes a list of all the countries to be used in the select tag for the news form
countries_list: List[str] = []
with open('app/countries.txt', 'r') as f:
    countries_list = f.readlines()


@app.route('/home')
@app.route('/')
def home() -> str:
    return render_template('index.html', content={'fa_code': fa_code})


@app.route('/news', methods=['GET', 'POST'])
@app.route('/news/<country>/<page>', methods=['GET', 'POST'])
def news(country: str = 'International', page: str = '1') -> str:
    if request.method == 'POST':
        country: str = request.form['country']
        page: str = request.form['page']
        # news: List[Dict[str, str]] = scrape_health_news(country, page)
        return redirect(url_for('news', country=country, page=page))

    news: List[Dict[str, str]] = scrape_health_news(country, page)
    return render_template('news.html',
                           content={
                               'news': news,
                               'countries': countries_list,
                               'fa_code': fa_code,
                               'page': page,
                               'country': country,
                           })


@app.route('/covid', methods=['GET', 'POST'])
@app.route('/covid/<country>', methods=['GET', 'POST'])
def covid_information(country: str = 'Global'):
    if request.method == 'POST':
        country: str = request.form['country']
        return redirect(url_for('covid_information', country=country))

    info: List[str] = scrape_covid_information(country)
    
    return render_template('covid.html',
                           content={
                               'info': info,
                               'country': country,
                               'fa_code': fa_code,
                               'countries': countries_list
                           })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
