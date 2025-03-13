## EFK for Kubernetes ##

![image](https://github.com/user-attachments/assets/0c26ed6d-5f2b-43a7-ae88-9246db7a9c30)

### Project Overview ###
This project sets up Fluentd as a log collector in a Kubernetes cluster to gather logs from application pods and send them to Elasticsearch for storage, indexing, and analysis. The setup enables centralized logging, making it easier to monitor, troubleshoot, and analyze application behavior.

### Components ###
- **Log Generator Application**
  - A sample application writing logs to `/app/logs/myapp.log` inside the *Pod* which is mapped to `/var/log/myapps/app.log` on the host.
 
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

