import os
import boto3
from dotenv import load_dotenv

# Using environment variables for S3 Credentials from .env file
# NOTE: It's a good practice to use environment variables for sensitive data in production.
load_dotenv()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

def get_s3_client():
    '''Method to create session and use s3 client.'''
    session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
    s3_client = session.client('s3')
    return s3_client

get_s3_client()

