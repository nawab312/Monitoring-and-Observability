```bash
kubectl port-forward -n monitoring prometheus-prometheus-kube-prometheus-prometheus-0  9090
kubectl port-forward -n monitoring svc/prometheus-prometheus-node-exporter 9100
```
- Then open `http://localhost:9090/targets` and look for a target **serviceMonitor/monitoring/prometheus-prometheus-node-exporter**
  - If Node Exporter is listed and "UP", it means Prometheus is collecting metrics.

- Access `http://localhost:9100/metrics`

![image](https://github.com/user-attachments/assets/c29f3a92-8080-41d6-9578-eba719369bb4)

**node_cpu_seconds_total** 
- Prometheus metric that counts how much time the CPU has spent doing different tasks (like working, waiting, or being idle) since the system started. It helps track CPU usage over time.
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

**node_filesystem_avail_bytes** 
- It is a Prometheus metric that shows the available disk space (in bytes) on a filesystem, considering user-specific restrictions. It helps monitor how much storage is free for use.
```
# HELP node_filesystem_avail_bytes Filesystem space available to non-root users in bytes.
# TYPE node_filesystem_avail_bytes gauge
node_filesystem_avail_bytes{device="/dev/nvme0n1p1",device_error="",fstype="xfs",mountpoint="/"} 8.0765386752e+10
node_filesystem_avail_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/09897e3c7576e3ceffa38e17ad87e675389ecac9ff6d3498c59f28f161059185/shm"} 6.7108864e+07
node_filesystem_avail_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/1f0703f217eae043e867275b984dbfa98bfb48ed0ee11443c152d87278b6db0b/shm"} 6.7108864e+07
node_filesystem_avail_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/201299aca5f35817a03242fcf41f4b0623d0229818025c4a7fbafddb20d817a7/shm"} 6.7108864e+07
node_filesystem_avail_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/2556b1acd8fc68eb7593c56ed581c3691c2d9396c3e40759b1cfbef861be315f/shm"} 6.7108864e+07
node_filesystem_avail_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/3ff7385bab28611347965c06f2e18acb73137d78569e660df0378ad9f867614f/shm"} 6.7108864e+07
node_filesystem_avail_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/444817514c4643e13c191af428656cf86138b5730763b42c7d5c340469e2b37c/shm"} 6.7108864e+07
node_filesystem_avail_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/7145dc9d1c95b7cb7374d8e8aadcb1a8d852fee8e536ab4d7af5a92e6c69742e/shm"} 6.7108864e+07
node_filesystem_avail_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/7eb7afa71aa3e6c8b8fe000a626be66d64ecfa2fa7e1f32e15c33cd46fe227ae/shm"} 6.7108864e+07
node_filesystem_avail_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/c9c6d31486bdabd978d73c02a3888b3b4628e47d233f7bb415b40aac2928f07e/shm"} 6.7108864e+07
node_filesystem_avail_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/df90d79aedb22a37a9f3da9ca368072b261b1e0776710450f47e61e7245a59ee/shm"} 6.7108864e+07
node_filesystem_avail_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/dfd1e7423ff87a616db28e2209f04555cbf06ecb2fbade14cb267f81d6dfdc0d/shm"} 6.7108864e+07
node_filesystem_avail_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/e692ae3676ce0593fb42a0aabba2209a988e9d8cb45c1da7d597dbcdea0dcec9/shm"} 6.7108864e+07
node_filesystem_avail_bytes{device="tmpfs",device_error="",fstype="tmpfs",mountpoint="/run"} 2.01484288e+09
```

**node_filesystem_size_bytes** 
- It is a Prometheus metric that shows the total size (in bytes) of a filesystem on a node. It helps monitor the total storage capacity available on a disk or partition.
```
# HELP node_filesystem_size_bytes Filesystem size in bytes.
# TYPE node_filesystem_size_bytes gauge
node_filesystem_size_bytes{device="/dev/nvme0n1p1",device_error="",fstype="xfs",mountpoint="/"} 8.5886742528e+10
node_filesystem_size_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/09897e3c7576e3ceffa38e17ad87e675389ecac9ff6d3498c59f28f161059185/shm"} 6.7108864e+07
node_filesystem_size_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/1f0703f217eae043e867275b984dbfa98bfb48ed0ee11443c152d87278b6db0b/shm"} 6.7108864e+07
node_filesystem_size_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/201299aca5f35817a03242fcf41f4b0623d0229818025c4a7fbafddb20d817a7/shm"} 6.7108864e+07
node_filesystem_size_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/2556b1acd8fc68eb7593c56ed581c3691c2d9396c3e40759b1cfbef861be315f/shm"} 6.7108864e+07
node_filesystem_size_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/3ff7385bab28611347965c06f2e18acb73137d78569e660df0378ad9f867614f/shm"} 6.7108864e+07
node_filesystem_size_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/444817514c4643e13c191af428656cf86138b5730763b42c7d5c340469e2b37c/shm"} 6.7108864e+07
node_filesystem_size_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/7145dc9d1c95b7cb7374d8e8aadcb1a8d852fee8e536ab4d7af5a92e6c69742e/shm"} 6.7108864e+07
node_filesystem_size_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/7eb7afa71aa3e6c8b8fe000a626be66d64ecfa2fa7e1f32e15c33cd46fe227ae/shm"} 6.7108864e+07
node_filesystem_size_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/c9c6d31486bdabd978d73c02a3888b3b4628e47d233f7bb415b40aac2928f07e/shm"} 6.7108864e+07
node_filesystem_size_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/df90d79aedb22a37a9f3da9ca368072b261b1e0776710450f47e61e7245a59ee/shm"} 6.7108864e+07
node_filesystem_size_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/dfd1e7423ff87a616db28e2209f04555cbf06ecb2fbade14cb267f81d6dfdc0d/shm"} 6.7108864e+07
node_filesystem_size_bytes{device="shm",device_error="",fstype="tmpfs",mountpoint="/run/containerd/io.containerd.grpc.v1.cri/sandboxes/e692ae3676ce0593fb42a0aabba2209a988e9d8cb45c1da7d597dbcdea0dcec9/shm"} 6.7108864e+07
node_filesystem_size_bytes{device="tmpfs",device_error="",fstype="tmpfs",mountpoint="/run"} 2.018967552e+0
```

**node_network_receive_bytes_total**
- It is a Prometheus metric that shows the total number of bytes received by a network interface since the system started. It helps monitor incoming network traffic on a node.
```
# HELP node_network_receive_bytes_total Network device statistic receive_bytes.
# TYPE node_network_receive_bytes_total counter
node_network_receive_bytes_total{device="eni1879ef520a0"} 2.117907e+06
node_network_receive_bytes_total{device="eni26d3491152b"} 6.636331e+07
node_network_receive_bytes_total{device="eni3d32f9273e1"} 6.217447e+06
node_network_receive_bytes_total{device="eni676e19a904c"} 1.0987614e+07
node_network_receive_bytes_total{device="eni870fcf0cca2"} 8.587832e+06
node_network_receive_bytes_total{device="eniabe29f7120a"} 4.93943e+06
node_network_receive_bytes_total{device="enibf9393385a8"} 8.620268e+06
node_network_receive_bytes_total{device="enicbae6532e16"} 2.131885e+06
node_network_receive_bytes_total{device="enifabf8079308"} 3.907524e+06
node_network_receive_bytes_total{device="eth0"} 6.5233035e+08
node_network_receive_bytes_total{device="eth1"} 1.8100576e+08
node_network_receive_bytes_total{device="eth2"} 4060
node_network_receive_bytes_total{device="lo"} 5.0695525e+07
```

![image](https://github.com/user-attachments/assets/a41d3603-f4cf-4f83-ba02-e6dc0f7d36e8)

### Grafana Setup ###

```bash
kubectl port-forward -n monitoring svc/prometheus-grafana 3000:80
```

- **CPU Usage** `100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)`
![image](https://github.com/user-attachments/assets/5a58203c-b626-4e67-9ff5-c8361b8d83f1)

- **Memory Usage:** `(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100`
![image](https://github.com/user-attachments/assets/90fd3f34-b8e4-4701-8380-dcdae75abbc7)

- **Disk Usage:** `(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100`
![image](https://github.com/user-attachments/assets/d7ece13c-7b2e-4066-bb4e-bef4a5b3e719)

- **Network Traffic:** `rate(node_network_receive_bytes_total[5m])`
![image](https://github.com/user-attachments/assets/b8171fba-0469-4b2b-bc76-57ea768a5bb3)



