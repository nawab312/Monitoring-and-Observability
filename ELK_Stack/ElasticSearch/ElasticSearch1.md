Create an index named Libray:
```bash
curl -X PUT "localhost:9200/library"
{"acknowledged":true,"shards_acknowledged":true,"index":"library"}
```

Add a Book Document:
```bash
curl -X POST "localhost:9200/library/_doc/1?pretty" -H 'Content-Type: application/json' -d'
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "published_year": 1925,
  "genre": "Fiction"
}
'
{
  "_index" : "library",
  "_id" : "1",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 0,
  "_primary_term" : 1
}
```

Add Another Book Document:
```bash
curl -X POST "localhost:9200/library/_doc/2?pretty" -H 'Content-Type: application/json' -d'
{
  "title": "1984",
  "author": "George Orwell",
  "published_year": 1949,
  "genre": "Dystopian"
}
'
{
  "_index" : "library",
  "_id" : "2",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 1,
  "_primary_term" : 1
}
```

Check Documents in the Index:
```bash
curl -X GET "localhost:9200/library/_search?pretty"
{
  "took" : 46,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "library",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "title" : "The Great Gatsby",
          "author" : "F. Scott Fitzgerald",
          "published_year" : 1925,
          "genre" : "Fiction"
        }
      },
      {
        "_index" : "library",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "title" : "1984",
          "author" : "George Orwell",
          "published_year" : 1949,
          "genre" : "Dystopian"
        }
      }
    ]
  }
}
```
#### Match Queries ####

**match_all**
```bash
curl -X GET "localhost:9200/library/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match_all": {}
  }
}
'
{
  "took" : 130,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "library",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "title" : "The Great Gatsby",
          "author" : "F. Scott Fitzgerald",
          "published_year" : 1925,
          "genre" : "Fiction"
        }
      },
      {
        "_index" : "library",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "title" : "1984",
          "author" : "George Orwell",
          "published_year" : 1949,
          "genre" : "Dystopian"
        }
      }
    ]
  }
}
```

**match**
```bash
curl -X GET "localhost:9200/library/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match": {
      "title": "gatsby"
    }
  }
}
'
{
  "took" : 24,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 0.5754429,
    "hits" : [
      {
        "_index" : "library",
        "_id" : "1",
        "_score" : 0.5754429,
        "_source" : {
          "title" : "The Great Gatsby",
          "author" : "F. Scott Fitzgerald",
          "published_year" : 1925,
          "genre" : "Fiction"
        }
      }
    ]
  }
}
```
