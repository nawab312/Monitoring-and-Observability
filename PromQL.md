**Types of Metrics**
- *Counter* Represents the total number of events since the application started (e.g., total HTTP requests handled). Only increases over time.
  - Counters can reset to 0 when an application or Pod restarts. `100 → 120 → 140 → (pod restart) → 5 → 20 → 40`
  - A naive calculation would think the metric dropped from 140 → 5, which would produce a negative rate.
  - However `rate()` detects counter resets by checking if the value suddenly decreases.
  - If a decrease is detected, Prometheus assumes: The counter restarted, not that the metric actually went negative.
  - So it ignores the drop and calculates the rate using the new counter sequence.
    ```code
    Before restart: 100 → 120 → 140
    After restart: 5 → 20 → 40
    ```

**Basics of PromQL**
- PromQL operates on time-series data and supports instant vector, range vector, scalar, and string types.
- Instant Vector: Fetches the latest value of a metric.
  ```bash
  node_cpu_seconds_total
  ```
- Range Vector: Fetches historical data within a time range.
  ```bash
  node_cpu_seconds_total[5m]
  ```
- Scalar: Returns a single numerical value.
  ```bash
  scalar(node_memory_MemTotal_bytes)
  ```

**Aggregation Functions**

![image](https://github.com/user-attachments/assets/c30922fc-2155-4bc6-984a-3ec8106d1b5a)

- Your app runs 3 replicas (pods), and each pod exposes the metric: `http_requests_total`. If you run this query: `rate(http_requests_total[5m])`. Grafana shows 3 separate lines on the graph. How would you modify the query to show the total request rate of the application across all pods as a single line?
  - `sum(rate(http_requests_total[5m]))`. Dont `rate(sum(http_requests_total)[5m])`. Always apply `rate()` first, then aggregate.

**Rate, Increase, and Delta Functions**
- These functions operate on range vectors.

![image](https://github.com/user-attachments/assets/e5a47d27-cf48-4da5-9bb3-925065d094fd)

- Your application running in Kubernetes exposes metrics and Prometheus is scraping them every 15 seconds. You create this PromQL query in Grafana: `rate(http_requests_total[5s])`. But the graph shows no data.
  - The query returns no data because the range window is smaller than the scrape interval.
  - The rate() function requires at least two data points in the time window to calculate a rate.

**Filtering and Label Matching**

![image](https://github.com/user-attachments/assets/6239cb5e-45a0-40f5-b541-6a855212ca70)

The **sum by (label)** function in PromQL is used to sum up metric values while preserving a specific label. It helps in aggregating data but keeps certain labels so that you can see meaningful groupings in your query results.
```bash
sum by (label) (metric)
```

Example: Summing CPU Usage Per Job
- Consider a metric cpu_usage that has multiple instances across different jobs.

![image](https://github.com/user-attachments/assets/2bdda500-309f-4bde-a42e-4cf90a1ff358)

```bash
sum by (job) (cpu_usage)
```
![image](https://github.com/user-attachments/assets/2fdbd963-ac66-4099-8176-ffe5c3744d09)


---

Decoding CPU Usage: `100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)`

- `node_cpu_seconds_total{mode="idle"}`
  - This metric comes from Node Exporter and represents the total cumulative seconds the CPU has spent in a given mode since boot.
  - It’s a counter.
- `rate(...[5m])`
  - Since it’s a counter, we take the per-second rate over the last 5 minutes.
  - For a single core, this value will be between 0 and 1.
- `avg by (instance)(...)`
  - Each CPU core exports its own time series.
 
---



