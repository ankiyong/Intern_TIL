import requests
from bs4 import BeautifulSoup

url = "http://hangul.thefron.me/"
res = requests.get(url)
soup =BeautifulSoup(res.text,"html.parser")
print(soup)

