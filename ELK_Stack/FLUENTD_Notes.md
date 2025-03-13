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
