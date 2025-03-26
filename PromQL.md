**Basics of PromQL**
- PromQL operates on time-series data and supports instant vector, range vector, scalar, and string types.
- Instant Vector: Fetches the latest value of a metric.
  ```bash
  node_cpu_seconds_total
  ```
- Range Vector: Fetches historical data within a time range.
  ```bash
  node_cpu_seconds_total[5m]
  ``
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


