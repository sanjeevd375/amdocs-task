# amdocs-task
This repo contains solution for the task provided by Amdocs.

### Codebase Setup

Step 1. Clone the public git repository. Use the command below in terminal.

      git clone https://github.com/sanjeevd375/amdocs-task.git
Step 2. Install Requirements

      pip install -r requirements.txt
Step 3: Create Environment file(.env) and add AWS Credentials.

      AWS_ACCESS_KEY = "<YOUR_ACCESS_KEY>T"
      AWS_SECRET_ACCESS_KEY = "<YOUR_SECRET_ACCESS_KEY>"  

### Code Execution

Step 1. Go inside Code directory.

Step 2. Edit "upload-to-s3" file to provide below basic details.
      
      S3_BUCKET = "<YOUR_S3_BUCKET_NAME>"
      SOURCE_FILE_PATH = "<PATH_TO_SOURCE_DATA_DIRECTORY>"
      S3_PATH = "<SUBDIRECTORY_PATH_IN_S3>"
      
      NOTE: Provide source file name in main function.

Step 3. Run below command in cmd for uploading file to s3.
      
      python "upload-to-s3.py"  
      
      

https://user-images.githubusercontent.com/45416838/147392664-026fbb61-3898-4e0c-b142-ce8d49a340e9.mp4

![aws-s3-upload](https://user-images.githubusercontent.com/45416838/147392711-05d2c0c3-0024-4c91-86f7-967b680bfa06.png)

Step 4. Edit "download-from-s3" file to provide below basic details.

      DEST_PATH = "<YOUR_DESTINATION_DIRECTORY>"
      S3_BUCKET = "<YOUR_S3_BUCKET_NAME>"
      DEST_FILE_NAME = "<TARGET_FILE_NAME>"
      S3_OBJECT_NAME = "S3_OBJECT_KEY_NAME"
      
Step 5. Run below command in cmd for downloading file from s3.

      python "download-from-s3.py" 

https://user-images.githubusercontent.com/45416838/147392990-df9ebf08-f564-4cba-91e8-db9adeaf21a5.mp4

![s3-download-local](https://user-images.githubusercontent.com/45416838/147393043-c94e8a73-7352-4e6d-82fc-547ac3c6ee41.png)


## Note: We can Implement above two methods to any python frameworks like Django,Flask or Falcon.

References:
### https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3.html
### https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1
