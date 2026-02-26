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

**Rate, Increase, and Delta Functions**
- These functions operate on range vectors.

![image](https://github.com/user-attachments/assets/e5a47d27-cf48-4da5-9bb3-925065d094fd)

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

