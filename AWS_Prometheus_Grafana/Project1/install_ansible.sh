#!/bin/bash
sudo apt update -y
sudo apt install -y ansible
echo "localhost ansible_connection=local" | sudo tee -a /etc/ansible/hosts
ansible-playbook /home/ubuntu/setup-prometheus.yml
