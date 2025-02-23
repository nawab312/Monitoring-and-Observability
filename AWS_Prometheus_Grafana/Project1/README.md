# Terraform + Ansible: Prometheus & Grafana Setup on AWS EC2 #

## Overview ##
- Terraform provisions the infrastructure (EC2 instances, security groups).
- Ansible configures the EC2 instance by installing Prometheus and Grafana.

```bash
terraform init
terraform apply --auto-approve
```
### Prometheus Targets ###
```<EC2_1_PUBLIC_IP>:9090/targets```

![Prometheus Targets](https://github.com/nawab312/Monitoring-and-Observability/blob/main/AWS_Prometheus_Grafana/Project1/Images/Prometheus_Targets.png)

## Grafana ##
- Access Grafana: ```http://<EC2-1-Public-IP>:3000``` (Default login: admin/admin)

### Add a new Prometheus data source ###
`http://loaclhost:9090`: Because Prometheus and Grafana are on same Server
Save and Test

![Prometheus Data Source](https://github.com/nawab312/Monitoring-and-Observability/blob/main/AWS_Prometheus_Grafana/Project1/Images/Grafana_Add_DataSource.png)
