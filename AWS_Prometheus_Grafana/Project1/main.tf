provider "aws" {
    region = "us-east-1"
}

resource "aws_instance" "ec2_1" {
    instance_type = "t2.micro"
    ami = "ami-02c78647b95a018b6"
    key_name = "myKey"
    security_groups = [aws_security_group.prometheus_grafana_sg.name]

    user_data = "${file("install_ansible.sh")}"

    tags = {
        Name = "EC2_Prom_Grafana"
    }
}

resource "aws_security_group" "prometheus_grafana_sg" {
    name = "prom_garfana_sg"
    description = "Allow Necessary Ports"

    ingress {
        from_port = 22
        to_port = 22
        cidr_blocks = ["0.0.0.0/0"]
        protocol = "tcp"
    }

    ingress {
        from_port = 9090
        to_port = 9090
        cidr_blocks = ["0.0.0.0/0"]
        protocol = "tcp"
    }

    ingress {
        from_port = 9090
        to_port = 9090
        cidr_blocks = ["0.0.0.0/0"]
        protocol = "tcp"
    }

    egress {
        from_port = 0
        to_port = 0
        cidr_blocks = ["0.0.0.0/0"]
        protocol = "-1"
    }

}
