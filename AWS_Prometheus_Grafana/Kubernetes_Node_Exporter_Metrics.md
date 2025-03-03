```bash
kubectl port-forward -n monitoring prometheus-prometheus-kube-prometheus-prometheus-0  9090
kubectl port-forward -n monitoring svc/prometheus-prometheus-node-exporter 9100
```

- Access `http://localhost:9100/metrics`

![image](https://github.com/user-attachments/assets/c29f3a92-8080-41d6-9578-eba719369bb4)

**node_cpu_seconds_total** 
- Prometheus metric that counts how much time the CPU has spent doing different tasks (like working, waiting, or being idle) since the system started. It helps track CPU usage over time.
- **CPU Usage** `100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)`
```
# TYPE node_cpu_seconds_total counter
node_cpu_seconds_total{cpu="0",mode="idle"} 8961.76
node_cpu_seconds_total{cpu="0",mode="iowait"} 6.78
node_cpu_seconds_total{cpu="0",mode="irq"} 0
node_cpu_seconds_total{cpu="0",mode="nice"} 1.02
node_cpu_seconds_total{cpu="0",mode="softirq"} 6.29
node_cpu_seconds_total{cpu="0",mode="steal"} 331.67
node_cpu_seconds_total{cpu="0",mode="system"} 126.04
node_cpu_seconds_total{cpu="0",mode="user"} 349.93
node_cpu_seconds_total{cpu="1",mode="idle"} 8961.93
node_cpu_seconds_total{cpu="1",mode="iowait"} 6.99
node_cpu_seconds_total{cpu="1",mode="irq"} 0
node_cpu_seconds_total{cpu="1",mode="nice"} 0.96
node_cpu_seconds_total{cpu="1",mode="softirq"} 5.96
node_cpu_seconds_total{cpu="1",mode="steal"} 329.77
node_cpu_seconds_total{cpu="1",mode="system"} 124.54
node_cpu_seconds_total{cpu="1",mode="user"} 350.99
```

**node_memory_MemTotal_bytes**
- It is a Prometheus metric that shows the total physical memory (RAM) available on a node in bytes.
```
# HELP node_memory_MemTotal_bytes Memory information field MemTotal_bytes.
# TYPE node_memory_MemTotal_bytes gauge
node_memory_MemTotal_bytes 4.0379392e+09
```

**node_memory_MemAvailable_bytes** 
- It is a Prometheus metric that shows the amount of memory (RAM) currently available for use on a node, including free memory and cached memory that can be reclaimed if needed.
```
# HELP node_memory_MemAvailable_bytes Memory information field MemAvailable_bytes.
# TYPE node_memory_MemAvailable_bytes gauge
node_memory_MemAvailable_bytes 2.670874624e+09
```

- **Memory Usage:** `(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100`


- Then open `http://localhost:9090/targets` and look for a target **serviceMonitor/monitoring/prometheus-prometheus-node-exporter**
  - If Node Exporter is listed and "UP", it means Prometheus is collecting metrics.

![image](https://github.com/user-attachments/assets/a41d3603-f4cf-4f83-ba02-e6dc0f7d36e8)

### Grafana Setup ###

```bash
kubectl port-forward -n monitoring svc/prometheus-grafana 3000:80
```
