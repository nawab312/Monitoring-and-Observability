# Terraform + Ansible: Prometheus & Grafana Setup on AWS EC2 #

## Overview ##
- Terraform provisions the infrastructure (EC2 instances, security groups).
- Ansible configures the EC2 instance by installing Prometheus and Grafana.

```bash
terraform init
terraform apply --auto-approve
```
### Changes According to Your Setup ###
In `setup_prometheus.yml` Here Instead of `172.31.89.143` use Private IP of your EC2_2 Instance
```bash
- job_name: 'node_exporter'
  static_configs:
    - targets: ['172.31.89.143:9100']
```

### Prometheus Targets ###
```<EC2_1_PUBLIC_IP>:9090/targets```

![Prometheus Targets](https://github.com/nawab312/Monitoring-and-Observability/blob/main/AWS_Prometheus_Grafana/Project1/Images/Prometheus_Targets.png)

## Grafana ##
- Access Grafana: ```http://<EC2-1-Public-IP>:3000``` (Default login: admin/admin)

#### Add a new Prometheus data source ####
`http://loaclhost:9090`: Because Prometheus and Grafana are on same Server
Save and Test

![Prometheus Data Source](https://github.com/nawab312/Monitoring-and-Observability/blob/main/AWS_Prometheus_Grafana/Project1/Images/Grafana_Add_DataSource.png)

#### Import Node Exporter Dashboard in Grafana ####
- Go to Dashboards → New → Import.
- Enter Dashboard ID: 1860 and click Load.
- Select Prometheus as the data source.
- Click Import.

![Grafana DashBoard](https://github.com/nawab312/Monitoring-and-Observability/blob/main/AWS_Prometheus_Grafana/Project1/Images/Grafana_Dashboard.png)
