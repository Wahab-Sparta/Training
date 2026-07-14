import boto3
import sys

#Our availability zone
region = "eu-west-1"

#Creates an S3 client
s3 = boto3.client("s3")

#takes arguments and saves as filename and bucket
filename, bucket = sys.argv[1], sys.argv[2]

#uploads the file with the same path to the bucket
s3.upload_file(filename, bucket, filename)

print(f"{filename} has been uploaded to {bucket}")
