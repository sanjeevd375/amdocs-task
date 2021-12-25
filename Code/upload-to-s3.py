import time
import boto3
from pathlib import Path
from boto3.s3.transfer import TransferConfig
from botocore.exceptions import ClientError
from helper import ProgressPercentage
from s3connect import get_s3_client

#Update below details as per your convenience
S3_BUCKET = "amdocs-test-files"
SOURCE_FILE_PATH = "/Users/ASUS/Desktop/Amdocs-Task/Test-data/"
S3_PATH = ""


def uploadFileS3(filename):
    '''
    Method to multipart upload large files into s3 bucket.
    Args :
        filename : Name of the file with extension
    Return: None    
    '''

    # Initialize s3 client
    s3_client = get_s3_client()

    try:
        file = SOURCE_FILE_PATH + filename
        key = S3_PATH + filename

        if not Path(file).is_file:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file)
 
        if key == "":
            raise ValueError("S3 object must be set!")
        
        print("Uploading [" + filename + "] to ["+ S3_BUCKET + "/"+ key + "].")

        # We can fine tune the below config as per requirement or can ce made generic. 
        config = TransferConfig(multipart_threshold=1024*1, max_concurrency=5,
                            multipart_chunksize=1024*3, use_threads=True)
        
        start = time.time()
        s3_client.upload_file(file, S3_BUCKET, key,
        ExtraArgs={ 'ACL': 'public-read', 'ContentType': 'video/mp4'},
        Config = config,
        Callback=ProgressPercentage(file, float(Path(file).stat().st_size))
        )
        end = time.time()
        print("\n\nFile Successfully Uploaded. Total time taken : ", time.strftime("%H:%M:%S", time.gmtime(end-start)))
    except ClientError as e:
        if e.response['Error']['Code'] == 'ExpiredToken':
                print('Login token expired')
    except boto3.exceptions.S3UploadFailedError as e:
            print("Failed to upload object!")
    except Exception as e:
            print(str(e))


def main():
    uploadFileS3('VID_20170303_153301.mp4')
    #uploadFileS3('AI.pdf')
    
if __name__ == "__main__":
    main()
