# Elasticsearch constant_score

constant_score를 처음 봐서 무엇인지 학습한 내용이다. 

일반적으로 검색 query를 사용하면 결과와 함께 score를 출력하고 이를 기준으로 출력 우선순위가 결정된다.

```json
#검색 query
GET my_index1/_search
{
  "query": {
    "term": {
      "name": {
        "value": "an"
      }
    }
  }
}
#결과
{
		"_index" : "my_index1",
        "_type" : "_doc",
        "_id" : "4",
        "_score" : 1.4552872,
        "_source" : {
          "name" : "an",
          "age" : 11,
          "gender" : "male",
          "title" : "Harry Potter and the Goblet of Fire"
        }
}
=> score가 계산되어 나온 것을 확인할 수 있다.
```

하지만 구조화된 데이터에서는 score를 굳이 산출하여 자원을 낭비할 필요가 없다. 그래서 constant_score 옵션을 통해 score계산을 하지 않고 1로 고정시킬 수 있다.

```json
#검색 query
GET my_index1/_search
{
  "query": {
    "constant_score": {
      "filter": {
        "match": {
          "name": "an"
        }
      },
      "boost": 1.2
    }
  }
}
#결과
      {
        "_index" : "my_index1",
        "_type" : "_doc",
        "_id" : "4",
        "_score" : 1.2,
        "_source" : {
          "name" : "an",
          "age" : 11,
          "gender" : "male",
          "title" : "Harry Potter and the Goblet of Fire"
     }
}
=> score는 기본적으로 1이 되고 boost로 지정한 1.2가 가중치로 계산되어 1.2의 score를 출력하고 있다.
```

### 결론

bool query 안에서 filter를 사용하는 것과 동일하다고 생각하면 될 것 같다. 단독으로 사용되기 보다는 bool query 안에서 다른 query와 결합되었을 때 강력한 힘을 발휘할 것으로 보인다. 