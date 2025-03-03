### CloudWatch Metrics on Grafana ###

**Install & Configure Grafana on EC2**
```bash
sudo apt-get update
sudo apt-get install -y adduser libfontconfig1
wget https://dl.grafana.com/oss/release/grafana_10.0.3_amd64.deb
sudo dpkg -i grafana_10.0.3_amd64.deb
sudo systemctl enable --now grafana-server
```
- Access Grafan `http://<your-ip>:3000` (Default login: `admin/admin`)

**Install CloudWatch Data Source Plugin**

![image](https://github.com/user-attachments/assets/0354c6f4-adca-4f11-abaa-430cfc259251)

**Create an AWS IAM Role for Grafana**
- Create an IAM Policy with read-only access to:
  - CloudWatch Metrics (EC2, RDS, EKS, ALB, etc.)
  - CloudWatch Logs (Log groups, log streams, log events)
  - CloudWatch Alarms

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:Describe*",
                "cloudwatch:List*",
                "cloudwatch:Get*",
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams",
                "logs:GetLogEvents",
                "logs:FilterLogEvents",
                "logs:StartQuery",
                "logs:GetQueryResults",
                "logs:StopQuery",
                "logs:TestMetricFilter"
            ],
            "Resource": "*"
        }
    ]
}
```

- Create an IAM Role for EC2 Instance (That has Grafann Running) and attach the above Policy
- Attach the IAM Role to the EC2 Instances.
- Now, your EC2 instance can directly access CloudWatch metrics without using access keys!
```bash
aws cloudwatch list-metrics --region us-east-1
```

**Grafana Setup**
- New Dashbaord -> Select *CloudWatch DataSource*
- NameSpace: `AWS/EC2`, Metric Name: `CPUUtilization`, Statistic: `Average`

![image](https://github.com/user-attachments/assets/c3fd6df6-578c-4aa1-9184-64ff6dece589)

  - 
