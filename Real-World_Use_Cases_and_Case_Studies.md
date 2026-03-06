- You deployed an application on Amazon Elastic Kubernetes Service.
- Your application suddenly becomes slow, but the pods are still running and no restarts are happening.

**SOLUTION**
- Goal is to locate the layer where latency is introduced: Application → Kubernetes → Node/Infrastructure.
- First Metrics to Check (Application Health)
  - Start with *request latency* and *error metrics*, not CPU.
  - Typical Prometheus metrics:
    ```code
    http_request_duration_seconds
    http_requests_total
    ```
  - Latency
    ```code
    rate(http_request_duration_seconds_sum[5m]) 
    /
    rate(http_request_duration_seconds_count[5m])
    ```
  - If latency increased but CPU is normal, the problem may be downstream dependency (DB/API).
- Check Kubernetes Resource Pressure
  -  CPU usage: `container_cpu_usage_seconds_total`
  -  CPU throttling: `container_cpu_cfs_throttled_seconds_total`
  -  If throttling increases: `CPU limit reached → container slowed down`
  -  Memory pressure: `container_memory_usage_bytes`, `container_memory_working_set_bytes`
- Node-Level Investigation (Infrastructure)
  ```code
  node_cpu_seconds_total
  node_load1
  node_memory_MemAvailable_bytes
  node_disk_io_time_seconds_total
  ```

  <img width="541" height="170" alt="image" src="https://github.com/user-attachments/assets/d0147d36-6988-4d61-afd0-111800412089" />
