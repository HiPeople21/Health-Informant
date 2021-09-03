from bs4 import BeautifulSoup
import requests
from typing import List, Dict


def scrape_health_news(country: str, page: str) -> List[Dict[str, str]]:
    '''
  Returns a dict of news items; the key being the contents and the value being the link
  '''

    # User-Agent for browser
    header: Dict[str, str] = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }

    # Variable in Google url called 'start' determined the page. 'start=0' means page 1, 'start=10' is page 2 ect.
    search_page: int = (int(page) - 1) * 10

    # Gets page markup
    html_text: str = requests.get(
        f'https://www.google.com/search?q=health+{country}&tbm=nws&start={search_page}',
        headers=header).text
    soup: str = BeautifulSoup(html_text, 'lxml')

    # G-cards hold the informantion needed
    news: List[str] = soup.find_all('g-card', class_='nChh6e')

    # Loops through all the g-cards and gets each value. This will allow styling and formatting of the text
    publishers: List[str] = [
        BeautifulSoup(str(i), 'lxml').find('div', class_='XTjFC WF4CUc').text
        for i in news
    ]
    titles: List[str] = [
        BeautifulSoup(str(i), 'lxml').find('div', class_='JheGif nDgy9d').text
        for i in news
    ]
    links: List[str] = [
        BeautifulSoup(str(i), 'lxml').find('a').get('href') for i in news
    ]
    times: List[str] = [
        BeautifulSoup(str(i), 'lxml').find('span', class_='WG9SHc').text
        for i in news
    ]
    main_text: List[str] = [
        BeautifulSoup(str(i), 'lxml').find('div', class_='Y3v8qd').text
        for i in news
    ]

    # Code above does the same as code below

    # publishers: List[str] = []
    # titles: List[str] = []
    # links: List[str] = []
    # times: List[str] = []
    # main_text: List[str] = []
    # for i in news:
    #   new_soup = BeautifulSoup(str(i), 'lxml')
    #   links.append(new_soup.find('a').get('href'))
    # for i in news:
    #   new_soup = BeautifulSoup(str(i), 'lxml')
    #   titles.append(new_soup.find('div', class_='JheGif nDgy9d').text)
    # for i in news:
    #   new_soup = BeautifulSoup(str(i), 'lxml')
    #   publishers.append(new_soup.find('div', class_='XTjFC WF4CUc').text)
    # for i in news:
    #   new_soup = BeautifulSoup(str(i), 'lxml')
    #   times.append(new_soup.find('span', class_='WG9SHc').text)
    # for i in news:
    #   new_soup = BeautifulSoup(str(i), 'lxml')
    #   main_text.append(new_soup.find('div', class_='Y3v8qd').text)

    # Returns a list with dictionaries containing all the information
    filtered_news: List[Dict[str, str]] = [{
        'publisher': publishers[i],
        'title': titles[i],
        'link': links[i],
        'time': times[i],
        'text': main_text[i]
    } for i in range(len(times))]

    return filtered_news


def scrape_covid_information(country: str):
    """
  Scrapes Covid statistics from Google
  """

    # User-Agent for browser
    header: Dict[str, str] = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }

    # Gets page markup
    html_text: str = requests.get(
        f'https://www.google.com/search?q={country}+Coronavirus+stats',
        headers=header).text

    soup: str = BeautifulSoup(html_text, 'lxml')

    stats_table: List[str] = soup.find('table', class_='qyEGdc')

    new_soup: str = BeautifulSoup(str(stats_table), 'lxml')

    stats_html: List[str] = new_soup.find_all('td')

    stats: List[str] = [
        BeautifulSoup(str(i), 'lxml').find('span').text for i in stats_html
    ]

    # Code above same as code below

    # for i in stats_html:
    #   new_soup: str = BeautifulSoup(str(i), 'lxml')
    #   stats.append(new_soup.find('span').text)

    return stats




x = requests.get('https://www.worldometers.info/coronavirus/?zarsrc=130#countries').text
y = BeautifulSoup(x, 'lxml')
z = y.find_all('a', class_='mt_a')
a=[]
for i in z:
  a.append(i.text)
a.sort()
print(a)