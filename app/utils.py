from bs4 import BeautifulSoup
import requests
from typing import List

def scrape_health_news() -> List[str]:
  '''
  Returns a dict of news items; the key being the contents and the value being the link
  '''
  header: dict = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

  html_text: str = requests.get('https://www.google.com/search?q=health+ireland&tbm=nws', headers=header).text
  soup: str = BeautifulSoup(html_text, 'lxml')

  news: List[str] = soup.find_all('g-card', class_='nChh6e')
  # for new in news:
  #   imgs: str = new.find_all('div', class_='vC5xic')
  #   for img in imgs:
  #     img.replaceWith('')
  # for new in news:
  #   imgs: str = new.find_all('g-img', class_='vC5xic')
  #   for img in imgs:
  #     img.replaceWith('')
  # print(news)


  links = []
  for i in news:
    new_soup = BeautifulSoup(str(i), 'lxml')
    links.append(new_soup.find('a').get('href'))

  news = {i:j for i in news for j in links}
  return news

# print(scrape_health_news())
scrape_health_news()