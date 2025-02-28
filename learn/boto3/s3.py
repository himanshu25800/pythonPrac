
from botocore.exceptions import ClientError
import boto3
import os




def getAccessControlList():
    # Retrieve a bucket's ACL
    s3 = boto3.client('s3')
    result = s3.get_bucket_acl(Bucket='video-clipper')
    print(result)




def createBucket(bucketName , region=None):
    try:
        if region is None:
                    s3_client = boto3.client('s3')
                    s3_client.create_bucket(Bucket=bucketName)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucketName,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        print(f"{e}")
        return False



def listBucket():
      
    s3 = boto3.client('s3')

    response = s3.list_buckets()
    # print(response)
    for bucket in response['Buckets']:
        print(f'{bucket["Name"]}')

    # or 
    # s3_resources = boto3.resource('s3')

    # for bucket in s3_resources.buckets.all():
    #     print(bucket.name)

def uploadFile(fileName,bucketName,objectName=None):

    if objectName == None :
        objectName = os.path.basename(fileName)

    s3 = boto3.client('s3')

    try:
        response = s3.upload_file(fileName,bucketName,objectName)
    except ClientError as e:
        print(f"{e}")
        return False

    return True


         

# uploadFile("file1.avif","pasta-bucket-2702",'firstUpload.avif')

# createBucket("pasta-bucket-2702")


# listBucket()
# getAccessControlList()