from elasticsearch import Elasticsearch,helpers
import json
def create_index(name,mapping,es):
    index = name
    with open(f'C:/Users/pop24/Desktop/source_code/python/elasticsearch/mapping/{mapping}.json','r') as f:
        mapping = json.load(f)
    es.index(index=index,body=mapping)

def search_template(es,templates):
    with open(f'C:/Users/pop24/Desktop/source_code/python/elasticsearch/mapping/{templates}.json','r') as f:
        body = json.load(f)
    es.put_script(id='search_template', body=body)
    return body



def get_info():
    floor = input("층");addr = input("주소");cate = input("분류");site = input("지점");name = input("상호")
    body = {
    "id" : "search_template",
    "params" : {
      "floor_level" : floor,
      "address" : addr,
      "address_operator" : "or",
      "category" : cate,
      "category_operator" : "or",
      "site_name" : site,
      "store_name" : name
        }
    }
    return body
 

def search_data(es,name):
    body = get_info()
    results = es.search_template(index=name, body = body)
    print(results)
    



# def inserg_data(name,mapping,csv_n):
#     es = Elasticsearch("localhost:9200")
#     if es.indices.exists(index=name):
#         with open(f'C:/Users/pop24/Desktop/source_code/python/elasticsearch/mapping/{csv_n}.json') as f:
#         reader = csv.DictReader(f)
#         helpers.bulk(es, reader, index=f"{name}", raise_on_error=False)

#     else:
#         name = create_index(name,mapping)
#         with open(f'C:/Users/pop24/Desktop/source_code/python/elasticsearch/mapping/{csv_n}.json') as f:
#         reader = csv.DictReader(f)
#         helpers.bulk(es, reader, index=f"{name}", raise_on_error=False)
    


