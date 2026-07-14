import boto3

#Our availability zone
region = "eu-west-1"

#Creates an S3 client
s3 = boto3.client("s3")

#Gets information of all the buckets
buckets = s3.list_buckets()

#For all the buckets in the dictionary, print all the names of buckets
for i in range(len(buckets["Buckets"])):
    print(buckets["Buckets"][i]["Name"])