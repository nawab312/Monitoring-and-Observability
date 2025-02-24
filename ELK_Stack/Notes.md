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
#### Match Queries ####
```bash
curl -X GET "localhost:9200/library/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match": {
      "title": "gatsby"
    }
  }
}
```

`_search` endpoint is used to search for documents within an index (or across multiple indices). 
```bash
curl -X GET "localhost:9200/library/_search?pretty"
```

**Example 1:** https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/ElasticSearch/ElasticSearch1.md


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



