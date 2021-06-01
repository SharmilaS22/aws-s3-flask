import os

import boto3
from botocore.client import Config
from decouple import config
from boto3 import client


AWS_ACCESS_KEY_ID     = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
REGION_NAME           = config("REGION_NAME")
BUCKET_NAME           = config("BUCKET_NAME")



client = boto3.client(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name = REGION_NAME
)
    
# Creating the high level object oriented interface
resource = boto3.resource(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name = REGION_NAME 
)

bucket = resource.Bucket(BUCKET_NAME)



def upload_file_handler(file_path, file_name):
    """
    Function to upload a file to an S3 bucket
    """

    bucket.upload_file(file_path, file_name)

    return "Uploaded Sucessfully"


def list_files_handler():
    """
    Function to list files in a given S3 bucket
    """
    contents = []
    for item in client.list_objects(Bucket=BUCKET_NAME)['Contents']:
        contents.append(item['Key'])

    return contents


def get_file_handler(file_name):
    """
    Function to get object from bucket
    """

    response = client.get_object(Bucket = BUCKET_NAME, Key = file_name)

    return response['Body']


def delete_file_handler(file_name):
    """
    Function to delete object from bucket
    """

    response = client.delete_object(Bucket = BUCKET_NAME, Key = file_name)
    
    return response['DeleteMarker']

def download_file(file_name, bucket):
    """
    Function to download a given file from an S3 bucket
    """
    s3 = boto3.resource('s3')
    output = f"downloads/{file_name}"
    s3.Bucket(bucket).download_file(file_name, output)

    return output

