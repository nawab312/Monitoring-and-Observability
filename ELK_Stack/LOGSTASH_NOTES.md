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

**Example1** https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/Logstash/Logstash1.md


