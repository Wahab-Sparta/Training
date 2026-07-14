import boto3
import sys

#Our availability zone
region = "eu-west-1"

#Creates an S3 client
s3 = boto3.client("s3")

#Takes name of bucket
bucket_name = sys.argv[1]

#Creates a bucket using the bucket name and the region
s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={"LocationConstraint":region})

print(f"Created a bucket {bucket_name}, in {region}")

