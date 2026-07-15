# AWS S3 Storage

- [AWS S3 Storage](#aws-s3-storage)
  - [What is a S3 storage](#what-is-a-s3-storage)
  - [Installing AWS CLI on Ubuntu 24.04 LTS](#installing-aws-cli-on-ubuntu-2404-lts)
  - [Configure AWS CLI](#configure-aws-cli)
  - [AWS CLI S3 Commands](#aws-cli-s3-commands)
  - [Python](#python)
  - [Python Scripts](#python-scripts)

<br>

## What is a S3 storage

* S3 stands for Simple Storage Services
* Used to store and retrieve any amount, at any time, from anywhere.
* Can easily be used to host a static website on the cloud.
* Provides built-in redundancy by default.
  * 3 copies - each one stored across the AZs in region.
* Accessible from AWS Console, AWS CLI (Command Line Interface), and Python Boto3.
* Often the resources for a website/application are stored in S3 e.g. images, log files.
* Default setting is files you put there are private, you need to configure to make them public.
* Completely separate from a VM.

## Installing AWS CLI on Ubuntu 24.04 LTS

1. ssh in and update & upgrade:
```
sudo apt update -y
sudo apt upgrade y
```

2. We will need unzip installed to unzip the AWS package
```
sudo apt install unzip
```
3. To install AWS CLI use this command:
```
Install AWS CLI:
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```
4. Check your version with:
aws --version

## Configure AWS CLI

To configure your AWS using CLI, use the command:
```
aws configure
```
You will then be prompted to:
* Enter your ID
* Enter your secret
* Enter your region e.g. eu-west-1
* Then enter json as the default output format

## AWS CLI S3 Commands
List buckets in AWS S3:  
```
aws s3 ls  
```
Get help on AWS:  
```
aws help
```
Get help for AWS S3 specifically:  
```
aws s3 help
```
<br>

To create an S3 bucket:  
```
aws s3 mb s3://tech610-wahab-first-bucket
```
List files in bucket:
```
aws s3 ls s3://tech610-wahab-first-bucket
```

Create a file with content & copy it into s3 bucket:
```
echo This is the first line in a test file > text.txt
aws s3 cp test.txt s3://tech610-wahab-first-bucket
```

Download files from bucket to machine:
```
aws s3 sync s3://<name of bucket> <path where you want the files downloaded>
EXAMPLE: aws s3 sync s3://tech610-wahab-first-bucket . 
```    
Note: The . means the current directory

Remove file from bucket:
```
aws s3 rm s3://tech610-wahab-first-bucket/test.txt
```

‼️WILL DELETE ALL FILES WITHOUT ASKING FOR CONFIRMATION  
Remove all files from bucket:
```
aws s3 rm s3://tech610-wahab-first-bucket --recursive
```
 
Delete a bucket:
```
aws s3 rb s3://tech610-wahab-first-bucket
```

‼️WILL DELETE ALL FILES AND THE BUCKET ITSELF WITHOUT ASKING FOR CONFIRMATION:  
Delete a bucket with files in it 
```
aws s3 rb s3://tech610-wahab-first-bucket --force
```

Note: 
If you use e.g. !23 you can redo a whole command without having to find it in your history

## Python
To be able to use Boto3 on Python to use AWS CLI, you need to install the dependencies pip and boto. We will also need a virtual environment for python.
```
sudo apt install python3.12-venv -y   #installs dependencies needed for venv
python3 -m venv my_scripts/env        #creates venv
source ~/my_scripts/env/bin/activate  #starts venv 
pip install pip --upgrade             #installs latest pip module
pip install boto3                     #installs boto3
```
## Python Scripts
[List all the S3 buckets](python_scripts/list_buckets.py)

[Create an S3 bucket](python_scripts/create_bucket.py)

[Upload data/file to an S3 bucket](python_scripts/upload_data.py)

[Download file from an S3 bucket](python_scripts/download_from_bucket.py)

[Delete file from an S3 bucket](python_scripts/delete_file.py)

[Delete an S3 bucket](python_scripts/delete_bucket.py)