### Custom Application Metrics Setup ###
**Understand Metric Types**
- **Counter:** Monotonically increasing value, ideal for counting events like requests or errors.
- **Gauge:** Represents a value that can go up or down, such as current memory usage.
- **Histogram:** Samples observations (e.g., request durations) and counts them in configurable buckets.
- **Summary:** Similar to histograms but also provides quantiles like median or percentiles.

**Instrument Your Application**
Integrate a Prometheus client library suitable for your programming language to define and expose metrics. For example, in Python:

```python
from prometheus_client import start_http_server, Counter
import random
import time

# Define a Counter metric to count the number of processed requests
REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests processed')

def process_request():
    """Simulate request processing by sleeping for a random amount of time."""
    time.sleep(random.random())
    REQUEST_COUNT.inc()  # Increment the request count

if __name__ == '__main__':
    # Start the Prometheus metrics server on port 8000
    start_http_server(8000)
    print("Prometheus metrics server started on port 8000")
    # Continuously process requests
    while True:
        process_request()
```

![image](https://github.com/user-attachments/assets/a1850913-9316-4b2e-b76d-2cafcab69b33)

```
# TYPE app_requests_total counter
app_requests_total 25.0
```

**Set Up Prometheus**
- `prometheus.yml`
```yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

alerting:
  alertmanagers:
    - static_configs:
        - targets: ['localhost:9093']

scrape_configs:
  - job_name: 'my_python_app'
    metrics_path: /metrics
    static_configs:
      - targets: ['localhost:8000']
```

- Start Prometheus Server
```bash
./prometheus --config.file=promeheus.yml
```
![image](https://github.com/user-attachments/assets/1659e784-3232-4686-970a-1018ac33851c)
