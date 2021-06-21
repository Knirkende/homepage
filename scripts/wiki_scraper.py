from bs4 import BeautifulSoup
import requests
import lxml
import re

URL = "https://no.wikipedia.org/wiki/Byggmester_Solness"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'lxml')

cont = soup.find('div', class_='mw-parser-output')

first_p = re.sub('\[\d\]', '', cont.find('p').get_text())

print(first_p)