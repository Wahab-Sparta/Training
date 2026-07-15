# Creating your own VPC

- [Creating your own VPC](#creating-your-own-vpc)
  - [Creating the VPC](#creating-the-vpc)
  - [Creating Public \& Private Subnets](#creating-public--private-subnets)
  - [Creating an Internet Gateway and attaching to VPC](#creating-an-internet-gateway-and-attaching-to-vpc)
  - [Creating a Route Table and adding routes](#creating-a-route-table-and-adding-routes)
  - [Creating the App and DB VMs](#creating-the-app-and-db-vms)

This document will be detailing how to create a 2 Tier VPC to run our Tic Tac Toe app with MongoDB.

Below will show how to:

1. Create a VPC
1. Create subnets
1. Create an internet gateway
1. Create a route table
1. Connect all the services mentioned for a secure VPC

---

![alt text](<Diagrams/Understanding VPCs.png>)

## Creating the VPC

1. Go to the [VPC homepage](https://eu-west-1.console.aws.amazon.com/vpcconsole/home?region=eu-west-1#Home:) on AWS and click "Create VPC".
1. Select "VPC only" and choose a suitable name.
1. Enter 10.0.2.0/16 as the IPv4 CIDR, then click "Create VPC".

## Creating Public & Private Subnets

1. Go to the [Subnets](https://eu-west-1.console.aws.amazon.com/vpcconsole/home?region=eu-west-1#subnets:) section of the VPC navigation tab and click "Create subnet".
1. Select the VPC you have just created.
1. Enter a name for your public subnet.
1. Select availability zone 1A.
1. In "IPv4 subnet CIDR block" enter "10.0.2.0/24".
   
   📝Note: This will allow 256 IP Addresses
1. Click "add new subnet".
2. Enter a name for your private subnet.
3. Select availability zone 1B.
4. In "IPv4 subnet CIDR block" enter "10.0.3.0/24".
5. Click "Create Subnet".

## Creating an Internet Gateway and attaching to VPC

1. Go to the [Internet gateways](https://eu-west-1.console.aws.amazon.com/vpcconsole/home?region=eu-west-1#igws:) section of the VPC navigation tab and click "Create internet gateway".
1. Enter a suitable name for your Internet Gateway and click "Create internet gateway".
1. At the top you will receive a notification, click "Attach to a VPC". If you do not see a notification, click "Actions" then click "Attach to a VPC".
1. Select your VPC, then click "Attach internet gateway".

## Creating a Route Table and adding routes

1. Go to the [Route tables](https://eu-west-1.console.aws.amazon.com/vpcconsole/home?region=eu-west-1#RouteTables:) section of the VPC navigation tab and click "Create route table".
1. Enter a suitable name for the public Route Table and then choose your VPC.
1. Click "Create route table".
1. First we will associate our newly created public subnet with this public route table. Click on "Subnet associations".
1. Click on "Edit subnet associations".
1. Select your public subnet and click "Save associations".
1. Secondly, we will create a route to our internet gateway. Click on "Edit routes".
1. Click "Add route" and enter "0.0.0.0/0" for the Destination.
1. Enter "Internet Gatway" for the Target, then below choose your Internet Gateway.
1. Click "Save changes".

## Creating the App and DB VMs

Now that you have created your VPC you can now create your App and DB VMs.  

You will need to create security groups for these when creating your VMs.  

First create your DB VM using your AMI since you will not have access to the internet.

Remeber to edit the Network settings and choose the VPC you created. Select the Private Subnet for the DB VM.

For the security groups, create a rule for Port 27017 with the Source as your public subnet CIDR "10.0.2.0/24". This will allow any machine in the public subnet to connect to the DB VM.