## ElasticSearch ##
A distributed search and analytics engine. Stores data in **JSON format** and allows full-text search
![ElasticSeach](https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/Images/ElasticSearch.png)

- Cluster: A collection of one or more nodes working together.
- Node: A single server in the Elasticsearch cluster. Types of Nodes
  - Master Node: Manages cluster-wide operations (e.g., creating indices, adding/removing nodes).
  - Data Node: Stores data and handles CRUD operations and search queries
  - Client Node: Acts as a load balancer for coordinating requests.
- Shard: basic units of data storage in Elasticsearch, and they are used to distribute data across the nodes in an Elasticsearch cluster. When an index is created, it is divided into smaller parts called shards.
  - Primary Shard: A primary shard is where the actual data is stored. Elasticsearch splits data into primary shards during the indexing process.
  - Sharding for Scalability: By dividing data into shards, Elasticsearch can distribute the load and data across multiple nodes in a cluster, making it scalable. This allows Elasticsearch to handle large volumes of data efficiently, as each shard can be stored and queried independently.  

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



