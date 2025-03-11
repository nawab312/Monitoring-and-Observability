## Centralized Logging in Kubernetes with ELK and Fluentd ##

Centralized logging is crucial for monitoring and debugging applications running in Kubernetes. 
In a distributed system, logs from different services need to be collected, aggregated, and visualized efficiently.
The ELK stack (Elasticsearch, Logstash, Kibana) is a powerful solution for this purpose, and Fluentd is used as a log forwarder.

**Architecture Overview**
- Application Pod: A simple microservice (Spring Boot) that generates structured JSON logs.
- Fluentd DaemonSet: Collects logs from all pods in the cluster.
- Logstash: Processes and transforms logs before sending them to Elasticsearch.
- Elasticsearch: Stores logs for querying and analysis.
- Kibana: Provides a UI to visualize logs in Elasticsearch.
