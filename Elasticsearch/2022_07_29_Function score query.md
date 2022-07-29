# Function score query

특정 필드에 대한 가중치를 주기 위한 옵션이 존재한다고 해서 테스트 해봄

=> 필드의 값(숫자)에 직접 가중치를 줘서 스코어를 조정할 수 있다.

```python
#document에 9개의 직급을 random하게 지정해주고 그에 따른 가중치를 price field에 지정해준다.
es = Elasticsearch("localhost:9200")
docs = []
rank = ["사장","전무","상무","부장","차장","과장","대리","사원","인턴"]
for i in range(1000):
    r = random.choice(rank)
    if r == "사장": n = 10
    elif r == "전무": n = 9
    elif r == "상무": n = 8
    elif r == "부장": n = 7
    elif r == "차장": n = 6
    elif r == "과장": n = 5
    elif r == "대리": n = 4
    elif r == "사원": n = 3
    elif r == "인턴": n = 2
    docs.append(
        {"_index" : "com_rank",
        "_source" : {
            "rank" : r,
            "price" : n
            }
        }
    )
helpers.bulk(es,docs)
```

#### function_score

```json
#price 값에 대해 factor 값 만큼 modifier에 명시된 연산을 진행하여 socre에 반영해준다.
#이때 price field가 존재하지 않는 document에 대해서는 missing값 만큼 연산하여 score에 반영해준다.
GET com_rank/_search
{
  "query": {
    "function_score": {
      "field_value_factor": {
        "field": "price",
        "factor": 1.2,
        "modifier": "sqrt",
        "missing": 1
      }
    }
  }
}

=> price field에 저장된 숫자가 클수록 높은 출력 우선순위가 생기게 되어 상단에 노출된다.
```



이제 match 검색의 결과에 대해 score를 재조정하여 출력 우선순위를 조작하는 것을 해볼 것이다. 

###### *이전 프로젝트에서 사용한 news index를 사용하여 테스트 해볼 것임*

```json
#먼저 검색하고 싶은 내용을 상단의 function_score 부분에 작성한다.
#그리고 가중치를 주고싶은 field에 대해서 
GET news/_search
{
  "query": {
    "function_score": {
      "query": {
        "match": {
          "title": "삼성"
      }
    },
      "field_value_factor": {
        "field": "id",
        "factor": 1.3,
        "modifier": "sqrt",
        "missing": 1
      }
    }
  }
}
```



