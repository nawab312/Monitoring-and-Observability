## Logstash ##
An open-source server-side data processing pipeline that ingests, transforms, and forwards data to Elasticsearch, where it can be stored and queried.

### Logstash Architecture ###
- Input: Collects or receives data from a source (e.g., files, network ports, APIs).
- Filter: Processes and transforms the data (e.g., parsing, grok, enriching).
- Output: Sends the processed data to an output destination (e.g., Elasticsearch, files, stdout).

![Lostash Pipeline](https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/Images/Logstash_Pipeline.png)

#### Filebeat #### 
A lightweight shipper for forwarding and centralizing log data. It monitors the log files or locations you specify, collects log events, and forwards them to your Elasticsearch or Logstash cluster for indexing and further processing. Configure Filebeat by editing the filebeat.yml file,  found in **/etc/filebeat/filebeat.yml**

```bash
# Filebeat Input Configuration
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /var/log/*.log  # Adjust this path based on where your logs are located

# Output to Elasticsearch
output.elasticsearch:
  hosts: ["http://localhost:9200"]  # Elasticsearch URL
  username: "elastic"              # Elasticsearch username (if authentication is enabled)
  password: "your_password_here"   # Elasticsearch password (if authentication is enabled)
  index: "filebeat-%{+yyyy.MM.dd}"  # Dynamic index name with date format

# Logging Configuration for Filebeat itself
logging:
  level: info               # Log level for Filebeat
  to_files: true            # Log to files
  files:
    path: /var/log/filebeat  # Directory to store Filebeat logs
    name: filebeat          # Log file name prefix
    keepfiles: 7            # Keep 7 log files
    permissions: 0644       # File permissions for log files
```



