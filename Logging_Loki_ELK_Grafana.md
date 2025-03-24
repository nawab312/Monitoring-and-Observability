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

**ElasticSearch** https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/ELASTICSEARCH_NOTES.md

**FluentD** https://github.com/nawab312/Monitoring-and-Observability/blob/main/ELK_Stack/FLUENTD_Notes.md

**Kubernetes Log Collection with Fluentd and Elasticsearch** https://github.com/nawab312/Monitoring-and-Observability/tree/main/ELK_Stack/Projects/Project3#readme


