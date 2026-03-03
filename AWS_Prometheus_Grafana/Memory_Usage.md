- By default, EC2 does NOT publish memory usage to Amazon CloudWatch.
- EC2 metrics come from the hypervisor.
- Memory usage is inside the guest OS. AWS cannot see it unless you tell it.

### Use CloudWatch Agent ###
- Install CloudWatch Agent inside the EC2 instance.
- It collects memory usage, disk usage, swap usage, process metrics. Pushes them to CloudWatch as custom metrics

### Step-by-Step (Linux EC2) ###
- Install Agent
```bash
#On Amazon Linux:
sudo yum install amazon-cloudwatch-agent

#On Ubuntu:
sudo apt install amazon-cloudwatch-agent
```
- Attach IAM Role. Instance must have role with: `CloudWatchAgentServerPolicy`
- Create Config. Use wizard:
```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard
```
  - Select: Collect memory metrics, Collect disk metrics, Set interval (e.g., 60 seconds)
  - This generates JSON config file.
- Start Agent
```bash
sudo systemctl start amazon-cloudwatch-agent
```

Now metrics appear under:
Namespace: `CWAgent`
