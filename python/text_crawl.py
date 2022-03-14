from urllib import response
import urllib.request
import json
import requests

key = "4174677349706f70373455597a785a"
url = f"http://openapi.seoul.go.kr:8088/{key}/json/TbPublicWifiInfo/1/5/"

res = requests.get(url)

r_dict = json.loads(response.text)
print(r_dict)




# res = urllib.request.urlopen(url)
# json_str = res.read().decode('utf-8')
# data = json.loads(json_str)
# print(json.dumps(data, indent=4, ensure_ascii=False))