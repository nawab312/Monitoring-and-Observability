**Setup:** https://github.com/nawab312/Monitoring-and-Observability/blob/main/AWS_Prometheus_Grafana/Kubernetes_Monitoring_Observability.md

- Access **kube-state-metrics**, which exposes Kubernetes object-level metrics.
```bash
kubectl port-forward svc/prometheus-kube-state-metrics 8081:8080 -n monitoring
```

![image](https://github.com/user-attachments/assets/6036a827-07e5-4c33-b6fe-fce5de350a5e)

![image](https://github.com/user-attachments/assets/de671508-3b70-41c7-a8fe-450f812bf0c0)

- **New Dashboard** -> **Add Visualizations** -> **Select Prometheus Data Source**

- Write your Queries Here:

![image](https://github.com/user-attachments/assets/dd777090-4aef-41b5-851b-ac843e7c4140)

**Pod Metrics**
- Total Number of Running Pods `count(kube_pod_status_phase{phase="Running"})`
- Pods by Status (Running, Pending, Failed, Succeeded) `count by (phase) (kube_pod_status_phase)`
![image](https://github.com/user-attachments/assets/d589d30d-0229-4037-ac81-6cef77928931)


