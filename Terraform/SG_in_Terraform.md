# Creating a Security Group in Terraform

To create a security group in Terraform, you will need to use the "aws_security_group" resource.  
Inside this resource you will need to provide the name, description, and VPC ID.  
Below is an example of what a Security Group would look like in Terraform.

```
resource "aws_security_group" "tech610-wahab-tf-allow-port-22-3000-80"{
    name = "tech610-wahab-tf-allow-port-22-3000-80"
    description = "Allows traffic on port 22, 3000 and 80"
    vpc_id = var.vpc_id

    tags = {
        Name = "tech610-wahab-tf-allow-port-22-3000-80"
    }
}
```

As for the security rules, you can use the resource "aws_vpc_security_group_ingress_rule" and "aws_vpc_security_group_egress rule".  
Inside the resource, you will need to provide: 
1. The security group ID
2. A list of cidr blocks (cidr_blocks) or a single cidr block (cidr_ipv4)
3. The port range (to and from)
4. The IP protocol  

📝NOTE: Terraform by default removes the AWS default outbound rule which allows all traffic on any port.  
Below is an example of an inbound (ingress) rule and outbound (egress) rule.
```
resource "aws_vpc_security_group_ingress_rule" "allow_port_80" {
  security_group_id = aws_security_group.tech610-wahab-tf-allow-port-22-3000-80.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 80
  ip_protocol       = "tcp"
  to_port           = 80
}

resource "aws_vpc_security_group_egress_rule" "allow_all_traffic_ipv4" {
  security_group_id = aws_security_group.tech610-wahab-tf-allow-port-22-3000-80.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = -1
}
```
📝NOTE: Notice in the egress rule, you do not need to define the ports as "-1" in "ip_protocol" defines any port.

There is another way of creating security groups, however AWS recommends the above:

```
resource "aws_security_group" "web_sg" {
  name        = "web-security-group"
  description = "Security group for web server"
  vpc_id      = aws_vpc.main.id

  ingress {
    description = "Allow SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Allow HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow all outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "web-security-group"
  }
}
```