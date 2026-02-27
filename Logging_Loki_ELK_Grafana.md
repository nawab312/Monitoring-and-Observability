**Centralized Logging**
- Collecting, storing, and analyzing logs from multiple systems/applications in one place.
- Provides a unified view of all logs for debugging, auditing, and monitoring.

### ELK Stack ###
- ELK Stack is a set of open-source tools designed for centralized log management and analysis:

![image](https://github.com/user-attachments/assets/b7d894f1-a979-48b9-8f41-97fe076eb231)

**How Components Interact:**
- Logstash collects logs, processes them, and sends them to Elasticsearch.
- Elasticsearch indexes and stores the logs for search and analytics.
- Kibana visualizes the data from Elasticsearch through dashboards and graphs

![image](https://github.com/user-attachments/assets/4299b5b1-5e30-4967-9486-af412ae7b0e1)

## Logstash ##
An open-source server-side data processing pipeline that ingests, transforms, and forwards data to Elasticsearch, where it can be stored and queried.

### Logstash Architecture ###
- Input: Collects or receives data from a source (e.g., files, network ports, APIs).
- Filter: Processes and transforms the data (e.g., parsing, grok, enriching).
- Output: Sends the processed data to an output destination (e.g., Elasticsearch, files, stdout).

![Lostash Pipeline](https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/Images/Logstash_Pipeline.png)

#### Filebeat #### 
A lightweight shipper for forwarding and centralizing log data. It monitors the log files or locations you specify, collects log events, and forwards them to your Elasticsearch or Logstash cluster for indexing and further processing. Configure Filebeat by editing the filebeat.yml file,  found in **/etc/filebeat/filebeat.yml**. Simpler version of the **filebeat.yml** configuration that collects logs from a specific directory and sends them directly to Elasticsearch without any additional configurations.

```bash
# Filebeat Input Configuration
filebeat.inputs:
  - type: log
    paths:
      - /var/log/*.log  # Adjust this path based on your log file location

# Output to Elasticsearch
output.elasticsearch:
  hosts: ["http://localhost:9200"]  # Replace with your Elasticsearch URL
```

Command to test Filebeat configuration: `filebeat test config`
```bash
filebeat test config
Config OK
```

To test the connection to Elasticsearch or Logstash: `filebeat test output`
```bash
filebeat test output
elasticsearch: http://localhost:9200...
  parse url... OK
  connection...
    parse host... OK
    dns lookup... OK
    addresses: 127.0.0.1
    dial up... OK
  TLS... WARN secure connection disabled
  talk to server... OK
  version: 8.17.1
```

`journalctl -u filebeat -f` is used to display the real-time log output for the filebeat service.

**Filebeat Harvesters** 
After the configuration is set, Filebeat starts "harvesters" for each log file path defined in the configuration. A harvester is a lightweight worker that reads the logs from a file line-by-line.
- Each file being monitored is picked up by a separate harvester.
- Harvesters track the position of the log files, so only new logs are processed.
As Filebeat reads each log line, it processes the log entry and adds metadata such as the log file path, timestamp, and other attributes

**Logstash Pipeline**
- Input: The input plugins specify the source from where Logstash should read data. Examples include reading from files, databases, or network ports
- Filter: Filters process data to transform, enhance, or extract meaningful information.
- Output: The output plugins specify where the processed data should be sent. For example, you may send logs to Elasticsearch, files, or even another service.

### Example 1 ###
Create `logstash.conf` at path `/home/siddharth312/ELK_Stack`
```bash
#logstash.conf
input {
    stdin { }
}

filter {
    mutate {
        add_field => { "added_field" => "Test field added" }
    }
}

output {
    stdout{ codec => rubydebug }
}
```

Go to path `/home/siddharth312/ELK_Stack/logstash-8.17.1/bin`
```bash
./logstash -f /home/siddharth312/ELK_Stack/logstash.conf
```

After Logstash starts running, type some input in the terminal (such as Hello, Logstash!) and press Enter. Logstash will process this input and output the data along with the added field `added_field`.
```bash
Hello, Logstash!
{
    "added_field" => "Test field added",
       "@version" => "1",
        "message" => "Hello, Logstash!",
     "@timestamp" => 2025-02-25T05:32:35.993492407Z,
          "event" => {
        "original" => "Hello, Logstash!"
    },
           "host" => {
        "hostname" => "siddharth312-GF65-Thin-9SD"
    }
}
```

### View Logs in a File ###

Create `logstash.conf` at path `/home/siddharth312/ELK_Stack`
```bash
#logstash.conf
input {
    stdin { }
}

filter {
    mutate {
        add_field => { "added_field" => "Test field added" }
    }
}

output {
    file {
        path => "/home/siddharth312/ELK_Stack/output.log"
    }
}
```

Go to path `/home/siddharth312/ELK_Stack/logstash-8.17.1/bin`
```bash
./logstash -f /home/siddharth312/ELK_Stack/logstash.conf
```

After Logstash starts running, type some input in the terminal (such as Siddharth or Singh). Logstash will process this input and save the output in output.log
```bash
#output.log
{"event":{"original":""},"@version":"1","message":"","host":{"hostname":"siddharth312-GF65-Thin-9SD"},"added_field":"Test field added","@timestamp":"2025-02-25T05:35:40.697756177Z"}
{"event":{"original":"Siddharth"},"@version":"1","message":"Siddharth","host":{"hostname":"siddharth312-GF65-Thin-9SD"},"added_field":"Test field added","@timestamp":"2025-02-25T05:35:46.526707895Z"}
{"event":{"original":"Singh"},"@version":"1","message":"Singh","host":{"hostname":"siddharth312-GF65-Thin-9SD"},"added_field":"Test field added","@timestamp":"2025-02-25T05:36:00.839776933Z"}
```
### Parsing Apache Logs with GROK ###

Create `logstash.conf` at path `/home/siddharth312/ELK_Stack`
```bash
input {
    file {
        path => "/var/log/apache2/access.log"
        start_position => "beginning"
    }
}

filter {
    grok {
        match => { "message" => "%{IP:client_ip}" }
    }
}

output {
    stdout {
        codec => rubydebug
    }
}
```

Go to path `/home/siddharth312/ELK_Stack/logstash-8.17.1/bin`
```bash
./logstash -f /home/siddharth312/ELK_Stack/logstash.conf
```

After Logstash starts running, Access the apache page by using `localhost`. Logstash will process this input and output the `client_ip` 
```bash
{
      "@version" => "1",
     "client_ip" => "127.0.0.1",
         "event" => {
        "original" => "127.0.0.1 - - [25/Feb/2025:11:20:42 +0530] \"GET / HTTP/1.1\" 200 3460 \"-\" \"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0\""
    },
          "host" => {
        "name" => "siddharth312-GF65-Thin-9SD"
    },
           "log" => {
        "file" => {
            "path" => "/var/log/apache2/access.log"
        }
    },
       "message" => "127.0.0.1 - - [25/Feb/2025:11:20:42 +0530] \"GET / HTTP/1.1\" 200 3460 \"-\" \"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0\"",
    "@timestamp" => 2025-02-25T05:50:43.083079491Z
}
```
---

## ElasticSearch ##
A distributed search and analytics engine. Stores data in **JSON format** and allows full-text search
![ElasticSeach](https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/Images/ElasticSearch.png)

- Cluster: A collection of one or more nodes working together.
- Node: A single server in the Elasticsearch cluster. Types of Nodes
  - Master Node: Manages cluster-wide operations (e.g., creating indices, adding/removing nodes).
  - Data Node: Stores data and handles CRUD operations and search queries
  - Client Node: Acts as a load balancer for coordinating requests.
- Shard: Basic units of data storage in Elasticsearch, and they are used to distribute data across the nodes in an Elasticsearch cluster. When an index is created, it is divided into smaller parts called shards.
  - Primary Shard: A primary shard is where the actual data is stored. Elasticsearch splits data into primary shards during the indexing process.
  - Sharding for Scalability: By dividing data into shards, Elasticsearch can distribute the load and data across multiple nodes in a cluster, making it scalable. This allows Elasticsearch to handle large volumes of data efficiently, as each shard can be stored and queried independently.

#### How Shard Works ####
- Data Distribution: When you create an index in Elasticsearch, you specify the number of primary shards. If you specify 3 shards, the data will be divided into 3 separate primary shards, and each shard can be placed on different nodes for distribution.
- Query Distribution: When a query is executed, Elasticsearch will route the query to the appropriate shards across different nodes. Each shard processes the query and returns the result, which is then aggregated and presented to the user.

![Shards](https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/Images/Shards.png)

**Replicas** are copies of the primary shards, created to provide fault tolerance and high availability. They serve as redundant backups to ensure that data is available in case a primary shard or node fails.

**Replication** Elasticsearch allows you to specify the number of replica shards for each primary shard when creating an index. By default, an index has 1 replica (meaning there is one copy of each primary shard).

#### How Replicas Work ####
- Fault Tolerance: If a node containing a primary shard goes down, the replica on another node can be promoted to a primary, ensuring data is not lost.
- Read Scalability: Replicas can be queried in parallel with primary shards. This means that having more replicas can improve read performance by spreading the query load across multiple nodes.

**Index:** A collection of documents with similar characteristics. Comparable to a database table in relational databases

**Document:** A single piece of data stored in JSON format

**Field:** Key-value pairs within a document.

```bash
# Index: Library
# Document:
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "published_year": 1925,
  "genre": "Fiction"
}
# Fields: title, author, published_year, genre
```

Start ElasticSeacrh
```bash
~/ELK_Stack/elasticsearch-8.17.1/bin$ ./elasticsearch
```
```bash
$ curl -X GET "localhost:9200/"
{
  "name" : "node-1",
  "cluster_name" : "my-cluster",
  "cluster_uuid" : "u4KVwP98RZ-QzPykdeVExg",
  "version" : {
    "number" : "8.17.1",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "d4b391d925c31d262eb767b8b2db8f398103f909",
    "build_date" : "2025-01-10T10:08:26.972230187Z",
    "build_snapshot" : false,
    "lucene_version" : "9.12.0",
    "minimum_wire_compatibility_version" : "7.17.0",
    "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "You Know, for Search"
}
```
- Create an Index: `curl -X PUT "localhost:9200/index_name`
- Delete an Index: `curl -X DELETE "http://localhost:9200/index_name"`

`_search` endpoint is used to search for documents within an index (or across multiple indices).
- `curl -X GET "localhost:9200/index_name/_search"`

Get all documents from an Elasticsearch index, use the `_search` API with the `match_all` query
```bash
{
    "query": {
        "match_all": {}
    }
}
```

#### Querying with Elastic Search ####
- **match**: The most commonly used query for full-text search. It analyzes the input query and compares it to the text fields.
```bash
{
    "query": {
        "match": {
            "message": "Hello"
        }
    }
}
```
- **match_phrase**: Similar to match, but it ensures the words appear exactly in the same order as in the query (useful for phrase searches).
```bash
{
    "query": {
        "match_phrase": {
            "message": "Hello Siddharth"
        }
    }
}
```
- **match_phrase_prefix**: Similar to match_phrase, but allows for prefix matching of the last word in the phrase.
```bash
{
    "query": {
        "match_phrase_prefix": {
            "message": "Hello Sidd"
        }
    }
}
```

#### Mappings ####
Mappings define how fields are stored and indexed in Elasticsearch. Default Mapping Behavior: When you index data without explicitly defining a mapping, Elasticsearch automatically guesses the field types.
- keyword: Used for exact matching where the string is stored as-is, without any analysis or tokenization. It is typically used for fields that require precise matching, like IDs, emails, tags, product codes, and status values.
- Text: Used for full-text search where the string is analyzed, tokenized, and indexed by individual terms (words). It is meant for fields containing descriptive content, such as product descriptions, blog articles, and comments.
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

### Example 1 ###
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

### Example 2 ###
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

## FluentD ##
**Fluentd** is an *open-source data collector* designed to unify logging by collecting, transforming, and sending log data to various storage solutions like Elasticsearch, Kafka, and cloud-based log management services. It is commonly used for centralized logging in cloud-native environments, including Kubernetes.

**Fluentd Configuration (fluent.conf) Basics**

fluent.conf is the main configuration file for Fluentd. It defines how logs are collected, processed, and forwarded to different destinations. The configuration consists of three main sections:
- Input (`<source>`) – Defines where logs come from.
- Filter (`<filter>`) – Modifies or processes logs before sending them.
- Buffers -  Temporarily stores logs before forwarding them.
- Output (`<match>`) – Defines where logs should be sent.

```conf
<source>
  @type tail
  path /var/log/app.log
  pos_file /var/log/fluentd.pos
  tag app.logs
  format json
</source>

<filter app.logs>
  @type record_transformer
  <record>
    hostname "#{Socket.gethostname}"
  </record>
</filter>

<match app.logs>
  @type elasticsearch
  host elasticsearch
  port 9200
  logstash_format true
</match>
```

- **<source> Block – Collecting Logs**
  - `@type tail` → Tells Fluentd to tail (follow) a log file.
  - `path /var/log/app.log` → Specifies the file to read logs from (`/var/log/app.log`).
  - `pos_file /var/log/fluentd.pos` → Stores the last read position of the log file to *avoid duplicate processing* after Fluentd restarts.
  - `tag app.logs` → Assigns a tag (app.logs) to the logs, which helps in filtering and routing.
  - `format json` → Specifies that logs are in JSON format, allowing structured log processing.
  - Example Log Entry in `/var/log/app.log`:
    ```json
    {"message": "User login successful", "user": "john_doe", "status": "success"}
    ```

- **<filter> Block – Modifying Logs**
  - `<filter app.logs>` → Applies this filter only to logs with the tag app.logs.
  - `@type record_transformer` → Modifies logs before sending them to the destination.
  - `<record>` → Defines new fields to add to the logs.
  - `hostname "#{Socket.gethostname}"` → Adds a hostname field with the system's hostname.
  - After Filtering (Modified Log with hostname field):
    ```json
    {
      "message": "User login successful",
      "user": "john_doe",
      "status": "success",
      "hostname": "server-01"
    }
    ```

- **<match> Block – Sending Logs to Elasticsearch**
  - `<match app.logs>` → Matches all logs with the tag *app.logs*.
  - `@type elasticsearch` → Sends logs to Elasticsearch.
  - `host elasticsearch` → Connects to an Elasticsearch instance running at hostname elasticsearch.
  - `port 9200` → Sends logs to Elasticsearch's default port (9200)
  - `logstash_format true` → Formats logs in Logstash-compatible format (useful for Kibana dashboards).
  - Example Log in Elasticsearch:
    ```json
    {
      "@timestamp": "2025-03-13T12:34:56Z",
      "message": "User login successful",
      "user": "john_doe",
      "status": "success",
      "hostname": "server-01"
    }
    ```

## EFK for Kubernetes ##

![image](https://github.com/user-attachments/assets/0c26ed6d-5f2b-43a7-ae88-9246db7a9c30)

### Project Overview ###
This project sets up Fluentd as a log collector in a Kubernetes cluster to gather logs from application pods and send them to Elasticsearch for storage, indexing, and analysis. The setup enables centralized logging, making it easier to monitor, troubleshoot, and analyze application behavior.

### Components ###
- **Log Generator Application**
  - A sample application writing logs to `/app/logs/myapp.log` inside the *Pod* which is mapped to `/var/log/myapps/app.log` on the host.
  - Code for App https://github.com/nawab312/Monitoring-and-Observability/tree/main/ELK_Stack/Projects/Project2#readme
 
- **Fluentd DaemonSet**
  - Runs on every Kubernetes node.
  - Collects logs from `/var/log/myapps/app.log` on the host.
  - Uses a ConfigMap to define log processing rules.
  - Sends logs to Elasticsearch.

- **ElasticSearch**
  - Stores and indexes logs.

- **Kibana**
  - UI for visualizing and querying logs stored in Elasticsearch.
 
### How to Implement ###

**Log Generator Application**
- *Deployment.yaml* https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/Projects/Project3/LogGeneratorApp/Deployment.yaml
- *Service.yaml* https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/Projects/Project3/LogGeneratorApp/Service.yaml
```bash
kubectl apply -f Deployment.yaml
kubectl apply -f Service.yaml
```

**FluentD**
- *ConfigMap.yaml* https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/Projects/Project3/FluentD/ConfigMap.yaml
- *DaemonSet.yaml* https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/Projects/Project3/FluentD/DaemonSet.yaml
```bash
kubectl apply -f ConfigMap.yaml
kubectl apply -f DaemonSet.yaml
```

**ElasticSearch**
- *PVC.yaml* https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/Projects/Project3/ElasticSearch/PVC.yaml
- *Service.yaml* https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/Projects/Project3/ElasticSearch/Service.yaml
- *StatefulSet.yaml* https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/Projects/Project3/ElasticSearch/StatefulSet.yaml

**Kibana**
- *Kibana.yaml* https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/Projects/Project3/Kibana/Kibana.yaml
- Access Kibana `http://<minikube-ip>:30001`

![image](https://github.com/user-attachments/assets/afa5ea9c-d5cb-4ef4-b89d-d96b3fcd7138)





