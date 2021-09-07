# Original function for scraping Covid information

# def scrape_covid_information(country: str):
#     """
#   Scrapes Covid statistics from Google
#   """

#     # User-Agent for browser
#     header: Dict[str, str] = {
#         'User-Agent':
#         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
#     }

#     # Gets page markup
#     html_text: str = requests.get(
#         f'https://www.google.com/search?q={country}+Coronavirus+stats',
#         headers=header).text

#     soup: str = BeautifulSoup(html_text, 'lxml')

#     stats_table: List[str] = soup.find('table', class_='qyEGdc')

#     new_soup: str = BeautifulSoup(str(stats_table), 'lxml')

#     stats_html: List[str] = new_soup.find_all('td')

#     stats: List[str] = [
#         BeautifulSoup(str(i), 'lxml').find('span').text for i in stats_html
#     ]

#     # Code above same as code below

#     # for i in stats_html:
#     #   new_soup: str = BeautifulSoup(str(i), 'lxml')
#     #   stats.append(new_soup.find('span').text)

#     return stats
