**Key Metrics to Include**
- *RTT (Round Trip Time)* --> Time taken for a packet to reach a target and return --> Detects latency issues
- *Throughput* --> Amount of data transferred per unit time --> Indicates bandwidth utilization
    - Bandwidth = The maximum rate at which data can be transferred over a network connection, usually measured in bps (bits per second), Mbps, or Gbps.
    - Throughput = The actual amount of data successfully transferred over the network per unit of time.
    - Bandwith Utilization(%) = (Throughput)/(Bandwith) * 100
- *Packet Loss* --> % of lost packets --> Critical for voice/video and TCP
- *Jitter* --> Variation in packet latency --> 	Affects real-time apps like VoIP
    - Jitter is the variation in packet arrival time on a network. In simple terms, it's the inconsistency in delay when data packets travel from source to destination.
- *TCP Retransmissions* --> Retransmitted packets --> Indicates congestion or packet drops
- *DNS Resolution Time* --> Time to resolve DNS queries --> Sluggish DNS increases page load time
- *Connection Drops* --> Abruptly closed or failed connections --> Can signal app or infra instability
- *Latency by Region/Hop* --> Regional latency or hop bottlenecks --> Helps debug geo-specific issues

**A production environment is experiencing slow application response times. You suspect it’s a network issue. How would you go about identifying whether it’s a latency, jitter, or packet loss issue?**

*Measure Round Trip Time (RTT)*
- RTT helps detect latency issues — if it's too high, packets are taking too long to travel to the destination and back.
```bash
ping <target IP or hostname>
```
- Metric: `probe_duration_seconds` (from `blackbox_exporter`)
- Target: Application endpoint (http, tcp, or icmp)

*Check for Packet Loss*
- Packet loss can delay retransmissions, especially in TCP, and destroy quality in VoIP/streaming.
```bash
ping -c 100 <target>
# or use mtr
mtr -rwzbc100 <target>
```
- Packet loss > 1% is concerning for most apps
- Consistent loss at specific hops = network path issue
- Metric: `probe_icmp_loss_percent` (from `blackbox_exporter` using icmp)

*Measure Jitter*
- Even if latency is low, variation in delay (jitter) can cause VoIP, video, or real-time data issues.
- Jitter is mainly a concern for: Real-time application traffic over UDP like VoIP (Zoom, Skype), Video calls/Streaming, Online gaming
```bash
iperf3 -c <target> -u -b 1M -t 30 -i 1
```
- Use Prometheus recording rules to compute the standard deviation of RTT over time.
```bash
stddev_over_time(probe_duration_seconds[5m])
```

*Check Throughput & Bandwidth Utilization*
- If throughput is significantly less than available bandwidth, something is throttling — likely CONGESTION, TCP retransmits, or bad routing.
```bash
sar -n DEV 1 10
iftop
```

*Analyze TCP Retransmissions*
- Resending lost or unacknowledged data packets.
- You send data over the internet. The receiver is supposed to send back an acknowledgment (ACK). If that ACK doesn't come within a certain time (timeout), TCP assumes the packet was lost or corrupted.So, TCP retransmits (resends) that same data again.
```bash
netstat -s | grep retransmit
ss -s
```
- Grafana Panel (node_exporter)
```bash
rate(node_netstat_Tcp_RetransSegs[5m])
```

*Check DNS Resolution Time*
- High DNS resolution time slows first byte latency — i.e., page or API starts responding late.
```bash
dig <hostname>
```
Check `Query time`: — should be < 100ms
- Grafana Panel (via Blackbox or custom exporter)
```bash
probe_dns_lookup_duration_seconds
```

*Monitor for Connection Drops*
- Sudden disconnections affect TCP handshake, force re-establishing, and increase latency.
```bash
dmesg | grep drop
ss -s
netstat -an | grep TIME_WAIT
```
- Metrics: `node_netstat_Tcp_AbortOnTimeout` AND `node_netstat_Tcp_EstabResets`
- Alerts: `increase(node_netstat_Tcp_EstabResets[5m]) > 10`
- Frequent TCP resets or aborts = connections are being dropped

---

You are monitoring a large production network using Prometheus and Grafana. Over time, you've noticed increased packet loss and high jitter affecting your real-time applications (VoIP and video conferencing). After investigating using Blackbox Exporter and Prometheus metrics, you observe that the jitter values are highly inconsistent, especially when packet loss exceeds 2%. Based on these findings, which of the following resolutions would be most effective in addressing the packet loss and jitter issues?

- *Quality of Service (QoS)* ensures that time-sensitive traffic (like VoIP and video conferencing) gets priority over less important traffic (e.g., email, file downloads). By prioritizing the network traffic for real-time applications, you can reduce jitter and packet loss because those applications will be given precedence on the network, ensuring a more stable experience.

---

You’re managing the network for a production system that is experiencing intermittent high latency during specific hours of the day. You have access to Prometheus and Grafana for monitoring. After investigating, you notice that latency spikes coincide with high traffic, particularly during scheduled batch processing. What would be the most effective approach to resolve the issue?

- *Implement Load Balancing*: Load balancing means spreading the traffic across multiple servers so no single server gets overloaded. By doing this, you can avoid a situation where one server is struggling to handle too many requests, which helps reduce latency (slowness).

---

You notice that users from certain regions are reporting slower response times when accessing the core banking application hosted on AWS. You’re using Prometheus and Grafana for monitoring, and you want to diagnose if this is a geo-specific latency issue.
Which metric and approach would help you accurately identify and troubleshoot the root cause?

- Use Prometheus to track *RTT (Round Trip Time)* by region and visualize in Grafana. By tracking RTT by region, you can clearly see which areas are experiencing higher latency. Using Prometheus, you can collect RTT metrics (using tools like blackbox_exporter). Then in Grafana, you can create a region-wise dashboard to visualize the latency differences.

---

Your PNB Core Banking application on AWS is seeing intermittent connection drops between microservices running in different Availability Zones (AZs). You suspect network instability or transient failures across zones. You want to monitor and pinpoint the issue using Prometheus and Grafana.

- You’re facing intermittent connection drops—this means services start talking, then suddenly lose the connection. This could be due to:
    - Network issues between Availability Zones (AZs)
    - Packet drops
    - Short-term failures in service-to-service communication
- Prometheus node_exporter and blackbox_exporter can help monitor TCP connection attempts, timeouts, and failures.
- By collecting metrics like:
    - `tcp_connection_failures_total`
    - `probe_success` (from blackbox)
    - `probe_failed_due_to_tcp`

- `probe_success` is a metric exposed by the Prometheus blackbox_exporter, which checks if a network probe (like a ping, HTTP request, or TCP connection) was successful or not. It's a gauge metric that returns either: 1 → The probe was successful, 0 → The probe failed
    - Ping (ICMP): You want to check if your server is reachable.
        - If it responds to ping, probe_success = 1, If it doesn’t, probe_success = 0
    - HTTP Endpoint: You probe an HTTP service to check if it returns `200 OK`.
        - If it does → probe_success = 1
        - If it's `500` or times out → probe_success = 0
    - `probe_success{instance="https://pnb-core-app.aws.com"}`