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


# jar: requests.cookies.RequestsCookieJar = requests.cookies.RequestsCookieJar()
# jar.set('CGIC','EhQxQzFDSEJEX2VuSUU4MzdJRTgzNyKHAXRleHQvaHRtbCxhcHBsaWNhdGlvbi94aHRtbCt4bWwsYXBwbGljYXRpb24veG1sO3E9MC45LGltYWdlL2F2aWYsaW1hZ2Uvd2VicCxpbWFnZS9hcG5nLCovKjtxPTAuOCxhcHBsaWNhdGlvbi9zaWduZWQtZXhjaGFuZ2U7dj1iMztxPTAuOQ')
# jar.set('OGPC', '1151720448-1:19022591-1:')
# jar.set('CONSENT', 'YES+shp.gws-20210811-0-RC2.en+FX+329')
# jar.set('HSID', 'AZXnHMl1YtHS9c-le')
# jar.set('SSID','A4nxvZFY8GdtYxj6B')
# jar.set('APISID','s-hQxc9dSx6rtbwt/A5LwQOs-U43oTp55o')
# jar.set('SAPISID','MZ5_D-3qhqX0lHBQ/AABaLgyOt-Efe82j_')
# jar.set('__Secure-1PAPISID','MZ5_D-3qhqX0lHBQ/AABaLgyOt-Efe82j_')
# jar.set('__Secure-3PSIDCC','AJi4QfEMzZKr7HtQb2H2WWl5tvSxIt7IGKhTQ_usUKsmioPdrGK3yk-42TYth3I9kc4Du-HF0TQv')
# jar.set('SIDCC','AJi4QfG-Q6iKiMGts27JF540hH8yEqEXZBDLUldmGYygcsPdDYbMqQw4C4sXiAJXFxfqVwjv0n0')
# jar.set('DV','U5XOeoCS9ehIgIjjJVKBVqYxOjmRvZdRxOrOAf3KTAAAAGByNTkKG2nvKwAAAAgH7s-UDNE6IAAAAA')
# jar.set('__Secure-3PAPISID','MZ5_D-3qhqX0lHBQ/AABaLgyOt-Efe82j_ ')
# jar.set('SID','BgiiY0TfdaCg8ixRDOkitCD1S_aT2ijdIYCwxfrf9iZWp48Xw0knCPlt7WTnxnz0mvk23Q.')
# jar.set('__Secure-1PSID','BgiiY0TfdaCg8ixRDOkitCD1S_aT2ijdIYCwxfrf9iZWp48X5RkjxU9-vx4VDkn0bwi6WQ.')
# jar.set('__Secure-3PSID','BgiiY0TfdaCg8ixRDOkitCD1S_aT2ijdIYCwxfrf9iZWp48XrsFu95EIy7hy2oEemHMtXw.')
# jar.set('OTZ','6149907_52_56_123900_52_436380')
# jar.set('SEARCH_SAMESITE','CgQIwZMB')
# jar.set('1P_JAR','2021-09-12-08')
# jar.set('NID','223=l1l2oZm8rBSfbkTWGILy2dbsJARDa_oz3UtNGw_cC4YcuXe6pldSzvgjkU4cWDwuYHm_Mnukt0BTIe-RodtpDbRMOUFP23qiOP87-mOiYAHowGIvUX28-7NcNnGLN2kD822y-W3lA4hozU1iAUJLMF-IP1ZbzFTZEvNPtDn8dUBFFVWN9khVnMGw-OyxvN3yeT0FLpqhBujXckZUf_4OmLTslDWucJEPGGYlAr9LvFA9SJD5e3W9MdMK-OXcEgP3gFjA5gRIpiyy7U-hN7pz1f74TCvCY-lJDvCs7vzv0mEkAhO1ClbEJiGBMjjEQvY_qbMuCmJb-0GIR2oVbSxjz5_-IrPhnmqt_wkiu9LogmZ88qhWyK4cJrlqPCM')