**Observability** 
- Ability to understand the **internal state of a system(Application + Infra + Network)** by analyzing the data it produces, including logs, metrics, and traces. 
- With the help of Observability I can get following information:
  - What is the disk or CPU or Memory utilization of a particular node in my Kubernetes Cluster over the last 24 Hours. 
  - Out of 100 API Calls made to my application how many requests were success. It also involves why these API Requests are failing and how to fix them
- 3 Pillars of Observability:
  - **Monitoring(Metrics):** Involves tracking system metrics like CPU usage, memory usage, and network performance. Provides alerts based on predefined thresholds and conditions. Monitoring tells us what is happening.
  - **Logging(Logs):** Involves the collection of log data from various components of a system. Logging explains why it is happening.
  - **Tracing(Traces):** Involves tracking the flow of a request or transaction as it moves through different services and components within a system. Tracing shows how it is happening. Components of Trace
    - **Trace ID**
      - A unique identifier assigned to a single request that helps track its journey across multiple services.
      - Every span within the trace shares the same Trace ID.
    - **Spans**
      - Each operation (e.g., database query, API call) within a trace is represented by a span.
    - **Parent-Child Relationships**
      - Traces are hierarchical, meaning a request can have multiple spans linked in a parent-child structure.
      - Example:
        - Parent Span: User makes a request to a web service.
        - Child Spans: API calls another microservice, Microservice queries the database

![image](https://github.com/user-attachments/assets/43031f4a-ce6a-4bd6-bcd3-9b800ddcf9e2)

**Prometheus** https://github.com/nawab312/Monitoring-and-Observability/blob/main/Prometheus/Notes.md

**Grafana** https://github.com/nawab312/Monitoring-and-Observability/blob/main/Grafana/Notes.md



  
