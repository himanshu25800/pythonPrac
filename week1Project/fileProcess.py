import boto3
from botocore.exceptions import ClientError
import os
import io
import csv
import json

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

    def readFile(self , objectName):
        
        response = self.s3_client.get_object(Bucket = self.bucketName, Key=objectName)
        body = response['Body'].read()
        # print(body)
        return body.decode('utf-8')

    def writeFile(self, objectName , body):

        ext = s3.findExtension(objectName)
        
        putData = body
        if ext == '.csv':
            putData = s3.convertCSVToString(body)
        if ext == '.json':
            putData = s3.convertJsonToString(body)
        print(putData)

        object = self.s3_client.put_object(Bucket = self.bucketName , Key = objectName , Body=putData)

        print("written Successful.")
        # print(object)


    def updateFile(self, objectName , body):
        ext = s3.findExtension(objectName)
        
        existingContent = self.readFile(objectName)
        # print(existingContent)

        if ext == '.csv':
            putData = s3.convertCSVToString(body , existingContent)
        if ext == ".json":
            putData = s3.convertJsonToString(body , existingContent)


        object = self.s3_client.put_object(Bucket = self.bucketName , Key = objectName , Body=putData)
        
        # print(object)

    @staticmethod
    def findExtension(objectName):
        baseName = os.path.basename(objectName)
        # print(baseName)
        ext = os.path.splitext(baseName)[-1]
        # print(ext)
        return ext

    @staticmethod
    def convertCSVToString(body , existingContent=None):
            if(existingContent==None):
                output = io.StringIO()
            else :
                output = io.StringIO(existingContent)
            writer = csv.writer(output)
            writer.writerows(body)
            # print(output)
            return output.getvalue()
    
    @staticmethod
    def convertJsonToString(body , existingContent=None):
        if(existingContent==None):
            currentData = [body]
        else :
            currentData = json.loads(existingContent)
            currentData.update(body)

        output = io.StringIO()
        json.dump(currentData , output)
        print(output.getvalue())
        return output.getvalue() 
    

if __name__=='__main__':
    s3client = s3('week1-project')
    # s3client.createBucket()
    # s3client.deleteBucket()
    # s3client.listBucket()
    # s3client.uploadFile('uploads/car.csv')
    # s3client.deleteFile("/c/car.csv")
    # s3client.deleteFile("/.csv/car.csv")
    # s3client.deleteFile("/('car', '.csv')/car.csv")
    # s3client.downloadFile("/csv/car.csv")
    # body = s3client.readFile("/json/first.json")
    # print(body)
    # data = [['Jeep','Compass','2020']]
    # data = {
    #     "name":"himanshu",
    #     "age":20,
    #     "Location": "Noida"
    # }
    # s3client.writeFile("/json/first.json", body=data)
    
    # data = [['Jeep','Compass','2020']]
    # s3client.updateFile("/csv/car.csv",body=data)

    # data = {
    #     "name":"Gaurav",
    #     "age":20,
    #     "Location": "Noida"
    # }
    data = {
        "address":"xyx",
        "sdf":"abc"
    }
    s3client.updateFile("/json/first.json", body=data)

    # body = s3client.readFile("/json/first.json")
    # print(body)

    # s3client.listResource()
