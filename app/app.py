from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from utils import scrape_health_news, scrape_covid_information
from typing import List, Dict
import json


app: Flask = Flask(__name__, template_folder='templates')

# Makes a list of all the countries to be used in the select tag for the news form
countries_list: List[str] = []
with open('app/countries.txt', 'r') as f:
    countries_list = f.readlines()


@app.route('/home')
@app.route('/')
def home() -> str:
    return render_template('index.html', content={})


@app.route('/news', methods=['GET', 'POST'])
@app.route('/news/<country>', methods=['GET', 'POST'])
def news(country: str = 'International') -> str:
    if request.method == 'POST':
        country: str = request.form['country']
        return redirect(url_for('news', country=country))

    return render_template('news.html',
                           content={
                               'countries': countries_list,
                               'country_js': json.dumps(country),
                               'country': country,
                           })


@app.route('/covid', methods=['GET', 'POST'])
@app.route('/covid/<country>', methods=['GET', 'POST'])
def covid_information(country: str = 'World'):
    if request.method == 'POST':
        country: str = request.form['country']
        return redirect(url_for('covid_information', country=country))


    
    return render_template('covid.html',
                           content={
                               'country': country,
                               'country_js': json.dumps(country),
                               'countries': countries_list,
                           })

@app.route('/load-news', methods=['POST'])
def load_news():
  country: str = request.form['country']
  page: str = request.form['page']
  news: List[Dict[str, str]] = scrape_health_news(country, page)
  return make_response(jsonify(news))

@app.route('/load-covid-data', methods=['POST'])
def load_covid_data():
  country: str = request.form['country']
  info: List[str] = scrape_covid_information(country)
  info = [info[i] for i in [1, 2, 3, 4, 5, 6, 7, 8, 11, 13]]
  return make_response(jsonify(info))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
