from flask import Flask, render_template
from utils import scrape_health_news
from typing import List, Dict

app: Flask = Flask(__name__, template_folder='templates')

@app.route('/home')
@app.route('/')
def home() ->str:
  
  return render_template('index.html')

@app.route('/news')
def news() ->str:
  news: List[Dict[str, str]] = scrape_health_news()
  
  return render_template('news.html', content={'news': news})


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
