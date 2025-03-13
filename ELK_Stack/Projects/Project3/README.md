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


