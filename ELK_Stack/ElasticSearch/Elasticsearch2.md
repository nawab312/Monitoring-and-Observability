Imagine you're building an online store, and you have two fields: one for product codes and another for product descriptions.
- Product Code: This is a unique identifier for each product, like "ABC123".
- Product Description: This is a detailed text description of the product, such as "This is a quick brown fox that jumps over the lazy dog".

Create an index named Products:
```bash
curl -X PUT "localhost:9200/products" -H 'Content-Type: application/json' -d'
{
    "mappings": {
        "properties": {
            "product_code": {
                "type": "keyword"
            },
            "product_description": {
                "type": "text"
            }
        }
    }
}
'
```

Index a couple of products with these fields
```bash
curl -X POST "localhost:9200/products/_doc/1?pretty" -H 'Content-Type: application/json' -d'
{
    "product_code": "ABC123",
    "product_description": "This is my product"
}
'
{
  "_index" : "products",
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
```bash
curl -X POST "localhost:9200/products/_doc/2?pretty" -H 'Content-Type: application/json' -d'
{
    "product_code": "DEF456",
    "product_description": "This is her product"
}
'
{
  "_index" : "products",
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

Searching Example

**term**
```bash
curl -X GET "localhost:9200/products/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "term": {
        "product_code": "ABC123"
    }
  }
}
'
{
  "took" : 27,
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
    "max_score" : 0.6931471,
    "hits" : [
      {
        "_index" : "products",
        "_id" : "1",
        "_score" : 0.6931471,
        "_source" : {
          "product_code" : "ABC123",
          "product_description" : "This is my product"
        }
      }
    ]
  }
}
```

**match**
```bash
curl -X GET "localhost:9200/products/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match": {
        "product_description": "This is her"
    }
  }
}
'
{
  "took" : 2,
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
    "max_score" : 1.0577903,
    "hits" : [
      {
        "_index" : "products",
        "_id" : "2",
        "_score" : 1.0577903,
        "_source" : {
          "product_code" : "DEF456",
          "product_description" : "This is her product"
        }
      },
      {
        "_index" : "products",
        "_id" : "1",
        "_score" : 0.36464313,
        "_source" : {
          "product_code" : "ABC123",
          "product_description" : "This is my product"
        }
      }
    ]
  }
}
```


