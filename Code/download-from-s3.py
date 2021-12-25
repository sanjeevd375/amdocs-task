import time
from s3connect import get_s3_client
from helper import ProgressPercentage
from botocore.exceptions import ClientError

#To be updated accordingly
DEST_PATH = "../Test-data"
S3_BUCKET = "amdocs-test-files"

DEST_FILE_NAME = "abc.mp4"
S3_OBJECT_NAME = "VID_20170303_153301.mp4"

def downloadFileS3(filename):
    if filename == "":
        NEW_DEST_FILE_NAME = S3_OBJECT_NAME.split('/')[-1]
    else:
        NEW_DEST_FILE_NAME = filename

    # Initialize s3 client
    s3_client = get_s3_client()

    try:
        print("Downloading ["+ S3_BUCKET + "/"+ S3_OBJECT_NAME + "] to ["+ DEST_PATH + "/"+ NEW_DEST_FILE_NAME + "].")
        start = time.time()
        s3_client.download_file(
            Bucket = S3_BUCKET,
            Key = S3_OBJECT_NAME,
            Filename = DEST_PATH + "/" + NEW_DEST_FILE_NAME,
            Callback=ProgressPercentage(NEW_DEST_FILE_NAME, (s3_client.head_object(Bucket=S3_BUCKET, Key=S3_OBJECT_NAME))["ContentLength"])
            )
        end = time.time()
        print("\n\nFile Successfully Downloaded. Total time taken : ", time.strftime("%H:%M:%S", time.gmtime(end-start)))
    except ClientError as e:
        print(str(e))

def main():
    downloadFileS3(DEST_FILE_NAME)
    
if __name__ == "__main__":
    main()
        
