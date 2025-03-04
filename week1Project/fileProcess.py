import boto3
from botocore.exceptions import ClientError
import os

class s3:

    def __init__(self , bucketName):
        self.bucketName = bucketName
        self.s3_client = boto3.client('s3')

    def createBucket(self, region=None):
        try:
            if region is None:
                location = {'LocationConstraint': self.s3_client.meta.region_name}
                self.s3_client.create_bucket(Bucket=self.bucketName , CreateBucketConfiguration=location)
            else:
                location = {'LocationConstraint': region}
                self.s3_client.create_bucket(Bucket=self.bucketName,
                                        CreateBucketConfiguration=location)
        except ClientError as e:
            print(f"{e}")
            return False
        
    
    def deleteBucket(self , copyBucket = None):
        try :
            if copyBucket == None :
                response = self.s3_client.list_objects_v2(Bucket=self.bucketName)
                if 'Contents' in response:
                    for obj in response['Contents']:
                        self.s3_client.delete_object(Bucket=self.bucketName , Key = obj['Key'])
            else:
                response = s3.list_objects_v2(Bucket=self.bucketName)
                if 'Contents' in response:
                    for obj in response['Contents']:
                        self.s3_client.copy_object(Bucket=copyBucket , CopySource = f"/{self.bucketName}/{obj['Key']}" , Key = obj['Key'])
                        self.s3_client.delete_object(Bucket=self.bucketName , Key = obj['Key'])
        
            self.s3_client.delete_bucket(Bucket = self.bucketName)
            
            print(f"{self.bucketName} is deleted")
        
        except ClientError as e:
            print(f"{e}")
            return False         

    def listBucket(self):
        response = self.s3_client.list_buckets()
        # print(response)
        for bucket in response['Buckets']:
            print(f'{bucket["Name"]}')

    def listResource(self):
        response = self.s3_client.list_objects_v2(Bucket=self.bucketName)
        # print(response['Contents'])
    
        for obj in response['Contents']:
            # print(obj['Key'])
            print(obj)

    def uploadFile(self, fileName, objectName=None):

        if objectName == None :
            objectName = os.path.basename(fileName)
        
        ext = os.path.splitext(objectName)[-1]
        ext = ext.strip('.')
        try:
            response = self.s3_client.upload_file(fileName,self.bucketName,f"/{ext}/{objectName}")
            print(response)
        except ClientError as e:
            print(f"{e}")
            return False

        return True

    def deleteFile(self , objectName):
        response = self.s3_client.list_objects_v2(Bucket=self.bucketName)

        if 'Contents' in response:
            for obj in response['Contents']:
            #     object_key = obj['Key']
            #     # print(object_key.split('/'))[-1]
                if obj['Key'] == objectName:
                    self.s3_client.delete_object(Bucket=self.bucketName , Key = obj['Key'])
                    return True
            return False
        else:
            print(f"No contents found in {self.bucketName}")

    def downloadFile(self, objectName):
        ext = os.path.basename(objectName)
        ext = os.path.splitext(ext)[-1]
        with open(f"downloads/file{ext}","wb") as f:
          self.s3_client.download_fileobj(self.bucketName , objectName , f)

    


if __name__=='__main__':
    s3client = s3('week1-project')
    # s3client.createBucket()
    # s3client.deleteBucket()
    # s3client.listBucket()
    # s3client.uploadFile('uploads/car.csv')
    # s3client.deleteFile("/('car', '.csv')/objectName")
    s3client.downloadFile("/csv/car.csv")
    s3client.listResource()
