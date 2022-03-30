from bs4 import BeautifulSoup
import requests

url = "https://news.daum.net/breakingnews/society?page=1"
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser').find("ul",{"class" : "list_news2 list_allnews"}).find_all("li")
for a in soup:
    print(soup.find("a"))

# for num in range(1,101):
#     url = f"https://news.daum.net/breakingnews/society?page={num}"
    

