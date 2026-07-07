# Provisiong MongoDB on Ubuntu 24.04 VM

Alway use `#! /bin/bash` at the top of your bash script (especially when using it for user data on AWS) so Linux knows it needs to use the bash interpreter.

## Step 1
These commands will update the list of available packages (update) and update your installed packages to the newest versions (upgrade).
```
sudo apt update -y
sudo apt upgrade -y
```

## Step 2sys
This command will import the MongoDB public GPG key.
```
curl -fsSL https://pgp.mongodb.com/server-8.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg \
   --dearmor
```
A GPG key is used in Linux to verify the authenticity and integrity of software. This means it will ensure the application we are downloading was officially published by the developers and has not been corrupted by malicious third parties.

## Step 3
This command will create a list file, adding MongoDB to your list of available packages.
```
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] https://repo.mongodb.org/apt/ubuntu noble/mongodb-org/8.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.2.list
```

## Step 4
We need to run this update command to update our list of packages so MongoDB can be installed.
```
sudo apt update
```
## Step 5
This command will install MongoDB 8.2.5
```
echo Installing MongoDB...
sudo apt-get install -y \
   mongodb-org=8.2.5 \
   mongodb-org-database=8.2.5 \
   mongodb-org-server=8.2.5 \
   mongodb-mongosh \
   mongodb-org-shell=8.2.5 \
   mongodb-org-mongos=8.2.5 \
   mongodb-org-tools=8.2.5 \
   mongodb-org-database-tools-extra=8.2.5
echo Installed MongoDB!
```

## Step 6
The below command will show the status of MongoDB, we will primarily be using this to check if the database is running.
```
sudo systemctl status mongodb
```

This next command will start the database.
```
sudo systemctl start mongod
```

This command will start during system boot.
```
sudo systemctl enable mongod
```
## Step 7

These commands will:
1. Create a backup of the config file, in case it's needed
2. Replace the bindIp with 0.0.0.0, allowing any IP to be able to connect
```
sudo cp /etc/mongod.conf /etc/mongod.conf.bak
sudo sed -i 's|bindIp: 127.0.0.1|bindIp: 0.0.0.0|' /etc/mongod.conf
```

## Step 8

If you have already started MongoDB in Step 6, restart MongoDB using:

```
sudo systemctl restart mongod
```