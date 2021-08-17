from bs4 import BeautifulSoup
import requests
from typing import List, Dict

def scrape_health_news() -> List[Dict[str, str]]:
  '''
  Returns a dict of news items; the key being the contents and the value being the link
  '''
  header: Dict[str, str] = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

  html_text: str = requests.get('https://www.google.com/search?q=health+ireland&tbm=nws', headers=header).text
  soup: str = BeautifulSoup(html_text, 'lxml')

  news: List[str] = soup.find_all('g-card', class_='nChh6e')
  # url: start=0 first google page, start=10 second google page ect

  publishers: List[str] = []
  titles: List[str] = []
  links: List[str] = []
  times: List[str] = []
  main_text: List[str] = []
  for i in news:
    new_soup = BeautifulSoup(str(i), 'lxml')
    links.append(new_soup.find('a').get('href'))
  for i in news:
    new_soup = BeautifulSoup(str(i), 'lxml')
    titles.append(new_soup.find('div', class_='JheGif nDgy9d').text)
  for i in news:
    new_soup = BeautifulSoup(str(i), 'lxml')
    publishers.append(new_soup.find('div', class_='XTjFC WF4CUc').text)
  for i in news:
    new_soup = BeautifulSoup(str(i), 'lxml')
    times.append(new_soup.find('span', class_='WG9SHc').text)
  for i in news:
    new_soup = BeautifulSoup(str(i), 'lxml')
    main_text.append(new_soup.find('div', class_='Y3v8qd').text)
  

  filtered_news: List[Dict[str, str]] = [{'publisher': publishers[i], 'title': titles[i], 'link': links[i], 'time': times[i], 'text': main_text[i]} for i in range(len(times))]
  return filtered_news

# print(scrape_health_news())
scrape_health_news()