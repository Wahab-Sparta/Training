import boto3
import sys

#Our availability zone
region = "eu-west-1"

#Creates an S3 client
s3 = boto3.client("s3")

#Takes name of bucket
bucket_name, filename = sys.argv[1], sys.argv[2]


#Deletes file inside bucket
s3.delete_object(Bucket=bucket_name, Key=filename)

