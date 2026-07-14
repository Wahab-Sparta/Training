import boto3
import sys

#Our availability zone
region = "eu-west-1"

#Takes name of bucket
bucket_name = sys.argv[1]

s3 = boto3.resource("s3")
bucket = s3.Bucket(bucket_name)

# Delete all objects
bucket.objects.all().delete()

# Delete the bucket
bucket.delete()

print(f"{bucket_name} has been deleted")