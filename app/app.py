from flask import Flask, render_template, request, redirect, url_for
from utils import scrape_health_news
from typing import List, Dict

app: Flask = Flask(__name__, template_folder='templates')

@app.route('/home')
@app.route('/')
def home() ->str:
  return render_template('index.html')

@app.route('/news', methods=['GET', 'POST'])
def news() ->str:
  if request.method == 'POST':
    country: str = request.form['country']
    page: str = request.form['page']
    news: List[Dict[str, str]] = scrape_health_news(country, page)
    return redirect(url_for('news_country', country=country, page=page))
  else:
    news: List[Dict[str, str]] = scrape_health_news()
  return render_template('news.html', content={'news': news})

@app.route('/news/<country>/<page>', methods=['GET', 'POST'])
def news_country(country: str, page: str):
  if request.method == 'POST':
    country: str = request.form['country']
    page: str = request.form['page']
    news: List[Dict[str, str]] = scrape_health_news(country, page)
    return redirect(url_for('news_country', country=country, page=page))
  else:
    news: List[Dict[str, str]] = scrape_health_news(country, page)
  return render_template('news.html', content={'news': news})


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
