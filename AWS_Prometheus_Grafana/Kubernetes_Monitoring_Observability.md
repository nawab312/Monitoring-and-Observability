```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
```
```bash
helm repo update
```
```bash
helm install prometheus prometheus-community/kube-prometheus-stack -n monitoring
NAME: prometheus
LAST DEPLOYED: Mon Mar  3 10:04:55 2025
NAMESPACE: monitoring
STATUS: deployed
REVISION: 1
NOTES:
kube-prometheus-stack has been installed. Check its status by running:
  kubectl --namespace monitoring get pods -l "release=prometheus"

Get Grafana 'admin' user password by running:

  kubectl --namespace monitoring get secrets prometheus-grafana -o jsonpath="{.data.admin-password}" | base64 -d ; echo

Access Grafana local instance:

  export POD_NAME=$(kubectl --namespace monitoring get pod -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=prometheus" -oname)
  kubectl --namespace monitoring port-forward $POD_NAME 3000

Visit https://github.com/prometheus-operator/kube-prometheus for instructions on how to create & configure Alertmanager and Prometheus instances using the Operator.
```

```bash
kubectl get pods -n monitoring
NAME                                                     READY   STATUS    RESTARTS   AGE
alertmanager-prometheus-kube-prometheus-alertmanager-0   2/2     Running   0          4m1s
prometheus-grafana-67466f9d58-w4nkb                      3/3     Running   0          4m6s
prometheus-kube-prometheus-operator-ffbb877b8-snkrw      1/1     Running   0          4m6s
prometheus-kube-state-metrics-777cbf7bc8-f9wnv           1/1     Running   0          4m6s
prometheus-prometheus-kube-prometheus-prometheus-0       2/2     Running   0          4m
prometheus-prometheus-node-exporter-vpg6l                1/1     Running   0          4m6s
```

```bash
kubectl get pods -n monitoring
NAME                                                     READY   STATUS    RESTARTS   AGE
alertmanager-prometheus-kube-prometheus-alertmanager-0   2/2     Running   0          13m
prometheus-grafana-67466f9d58-w4nkb                      3/3     Running   0          13m
prometheus-kube-prometheus-operator-ffbb877b8-snkrw      1/1     Running   0          13m
prometheus-kube-state-metrics-777cbf7bc8-f9wnv           1/1     Running   0          13m
prometheus-prometheus-kube-prometheus-prometheus-0       2/2     Running   0          13m
prometheus-prometheus-node-exporter-vpg6l                1/1     Running   0          13m
```

**Alertmanager**
- Pod: `alertmanager-prometheus-kube-prometheus-alertmanager-0`
- Description: Handles alerts sent by Prometheus. It processes, deduplicates, groups, and routes them to external services (e.g., Slack, email, PagerDuty).

**Grafana**
- Pod: `prometheus-grafana-67466f9d58-w4nkb`
- Description: Web-based visualization tool for Prometheus metrics. Used for dashboards and monitoring.

**Prometheus Operator**
- Pod: `prometheus-kube-prometheus-operator-ffbb877b8-snkrw`
- Description: Manages Prometheus instances, Alertmanager, and related resources in Kubernetes.

**Kube State Metrics**
- Pod: `prometheus-kube-state-metrics-777cbf7bc8-f9wnv`
- Description: Exposes Kubernetes cluster metrics (e.g., pod count, node status, resource utilization) to Prometheus.

**Prometheus Server**
- Pod: `prometheus-prometheus-kube-prometheus-prometheus-0`
- Description: The core Prometheus instance that scrapes metrics from various sources and stores them.

**Node Exporter**
- Pod: `prometheus-prometheus-node-exporter-vpg6l`
- Description: Collects host-level metrics (CPU, memory, disk, network) from Kubernetes worker nodes.

```bash
# Access Prometheus http://localhost:9090.
kubectl port-forward -n monitoring prometheus-prometheus-kube-prometheus-prometheus-0 9090
```

```bash
# Access Grafana http://localhost:3000
kubectl port-forward -n monitoring svc/prometheus-grafana 3000
```

**Why Port Forwarding to a Pod (`prometheus-prometheus-kube-prometheus-prometheus-0`)?**
- **Reason: Prometheus is a StatefulSet**
- The Prometheus pod belongs to a **StatefulSet** (not a Deployment), meaning it has a **stable pod name**.
- Since **StatefulSet pods are unique and persistent**, you can directly forward to the pod.

**Why Port Forwarding to a Service (svc/prometheus-grafana)?**
- **Reason: Grafana is a Stateless Deployment**
- Grafana runs as a **Deployment**, meaning pods are dynamic and can change.
- Using a Service ensures you always connect to an available Grafana pod, even if the pod restarts.
