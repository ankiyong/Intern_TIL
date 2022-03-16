from this import d
import pandas as pd
import requests
from bs4 import BeautifulSoup
import pprint
# param_set = {"key" : "f75bc744a2d412f7ace5e5e133f74279",
#               "openStartDt" : 2000,
#               "itemPerPage" : 100000}
# key= "f75bc744a2d412f7ace5e5e133f74279"
# url = "https://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=f75bc744a2d412f7ace5e5e133f74279&openStartDt=2017&itemPerPage=100"

# res = requests.get(url)
# contents = res.text
# print(contents['movieListResult'])

# info = json.loads(contents)
# df = pd.json_normalize(info)


df = pd.read_csv('C:/Users/pop24/Desktop/source_code/python/movie.csv',engine='python',sep=',',quotechar='"',error_bad_lines=False)
print(df.columns)