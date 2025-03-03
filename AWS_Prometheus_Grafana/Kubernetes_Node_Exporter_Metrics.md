```bash
kubectl port-forward -n monitoring prometheus-prometheus-kube-prometheus-prometheus-0  9090
kubectl port-forward -n monitoring svc/prometheus-prometheus-node-exporter 9100
```

- Access `http://localhost:9100/metrics`

![image](https://github.com/user-attachments/assets/c29f3a92-8080-41d6-9578-eba719369bb4)

- Then open `http://localhost:9090/targets` and look for a target **serviceMonitor/monitoring/prometheus-prometheus-node-exporter**
  - If Node Exporter is listed and "UP", it means Prometheus is collecting metrics.

![image](https://github.com/user-attachments/assets/a41d3603-f4cf-4f83-ba02-e6dc0f7d36e8)

