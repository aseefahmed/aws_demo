import boto3

# Create a session using your AWS credentials


# Create an S3 client
s3 = boto3.client('s3')

# List all the buckets
response = s3.list_buckets()

# Print the bucket names
print("List of AWS S3 buckets:")
for bucket in response['Buckets']:
    print(bucket['Name'])