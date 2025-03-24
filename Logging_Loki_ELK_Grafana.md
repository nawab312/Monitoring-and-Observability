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

**Example 1:** https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/ElasticSearch/ElasticSearch1.md

#### Keyword and Text data type in Elasticsearch ####
- keyword: Used for exact matching where the string is stored as-is, without any analysis or tokenization. It is typically used for fields that require precise matching, like IDs, emails, tags, product codes, and status values.
- Text: Used for full-text search where the string is analyzed, tokenized, and indexed by individual terms (words). It is meant for fields containing descriptive content, such as product descriptions, blog articles, and comments.

**Example 2:** https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/ElasticSearch/Elasticsearch2.md








**FluentD** https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/FLUENTD_Notes.md

**Kubernetes Log Collection with Fluentd and Elasticsearch** https://github.com/nawab312/Monitoring-and-Observability/tree/main/ELK_Stack/Projects/Project3#readme


