
from botocore.exceptions import ClientError
import boto3
import os



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


def deleteBucket(bucketName , copyBucket=None):
    s3 = boto3.client('s3')
    try :
        if copyBucket == None :
            response = s3.list_objects_v2(Bucket=bucketName)
            if 'Contents' in response:
                for obj in response['Contents']:
                    s3.delete_object(Bucket=bucketName , Key = obj['Key'])
        else:
            response = s3.list_objects_v2(Bucket=bucketName)
            if 'Contents' in response:
                for obj in response['Contents']:
                    s3.copy_object(Bucket=copyBucket , CopySource = f"/{bucketName}/{obj['Key']}" , Key = obj['Key'])
                    s3.delete_object(Bucket=bucketName , Key = obj['Key'])
        s3.delete_bucket(Bucket = bucketName)
        print(f"{bucketName} is deleted")
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





def getAccessControlList(bucketName):
    # Retrieve a bucket's ACL
    s3 = boto3.client('s3')
    result = s3.get_bucket_acl(Bucket=bucketName)
    print(result)

def getBucketPolicy(bucketName):
    # Retrieve the policy of the specified bucket
    s3 = boto3.client('s3')
    result = s3.get_bucket_policy(Bucket=bucketName)
    print(result)
    # print(result['Policy'])


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


def searchObject(bucketName, objectName):

    s3 = boto3.client('s3')
    
    response = s3.list_objects_v2(Bucket=bucketName)

    if 'Contents' in response:
        for obj in response['Contents']:
            object_key = obj['Key']
            # print(object_key.split('/'))[-1]
            if object_key.split('/')[-1] == objectName:
                return True
        return False
    else:
        print(f"No contents found in {bucketName}")


def downloadFile(bucketName , objectName , file):
    s3 = boto3.client('s3')

    s3.download_file(bucketName, objectName , file)


def downloadFileWithBinaryData(bucketName , objectName , file):
     s3 = boto3.client('s3')

     with open(file,"wb") as f:
          s3.download_fileobj(bucketName , objectName , f)



def listBucketResource(bucketName):
    s3 = boto3.client('s3')

    response = s3.list_objects_v2(Bucket=bucketName)
    # print(response['Contents'])
    
    for obj in response['Contents']:
        # print(obj['Key'])
        print(obj)


def configureLifeCycleRules(bucketName , lifecyclePolicy):
    s3 = boto3.client('s3')

    try:
        s3.put_bucket_lifecycle_configuration(
        Bucket=bucketName,
        LifecycleConfiguration=lifecyclePolicy)
    except ClientError as e:
        print(f"{e}")


def getLifeCycleRules(bucketName):
    s3 = boto3.client('s3')
    response = s3.get_bucket_lifecycle_configuration(Bucket=bucketName)
    # print(response)
    print(response['Rules'])


def enableVersioning(bucketName):

    s3 = boto3.client('s3')
    s3.put_bucket_versioning(
    Bucket=bucketName,
    VersioningConfiguration={
        'Status': 'Enabled'
        }
    )

    print(f"Versioning has been enabled for {bucketName}")

def disableVersioning(bucketName):
    s3 = boto3.client('s3')
    s3.put_bucket_versioning(
    Bucket=bucketName,
    VersioningConfiguration={
        'Status': 'Suspended'
    }
    )

    print(f"Versioning has been suspended for {bucketName}")


def enableLogging(sourceBucket , targetBucket):
    s3 = boto3.client('s3')


    # Enable logging on the source bucket
    s3.put_bucket_logging(
        Bucket=sourceBucket,
        BucketLoggingStatus={
            'LoggingEnabled': {
                'TargetBucket': targetBucket,
                'TargetPrefix': 'logs/'  # Prefix for log files
            }
        }
    )
    print(f"Logging Enabled for {sourceBucket}")

def disableLogging(sourceBucket):

    s3 = boto3.client('s3')

    s3.put_bucket_logging(
        Bucket=sourceBucket,
        BucketLoggingStatus={
            'LoggingEnabled': {}
        }
    )

    print(f"Logging has been disabled for {sourceBucket}")

listBucketResource("pasta-bucket-0303")

# print(searchObject('video-clipers','3ff60913-5fcb-4e76-b944-a99ef8b5ac30'))

# downloadFile("pasta-bucket-2702",'firstUpload.avif',"file2.avif",)

# downloadFileWithBinaryData('pasta-bucket-2702','firstUpload.avif','file3.avif')

# uploadFile("file1.avif","pasta-bucket-2702",'firstUpload.avif')

# createBucket("log-bucket-0303","ap-south-1")


# listBucket()
# getAccessControlList(bucketName="pasta-bucket-2702")
# deleteBucket(bucketName="pasta-bucket-2702" , copyBucket="pasta-bucket-0303")

# getBucketPolicy(bucketName="video-clipers")


# lifecyclePolicy = {
#     'Rules': [
#         {
#             'ID': 'Move-to-IA-after-30-days',
#             'Prefix': '',  # Apply the rule to all objects in the bucket
#             'Status': 'Enabled',
#             'Transitions': [
#                 {
#                     'Days': 30,  # Transition after 30 days
#                     'StorageClass': 'STANDARD_IA'  # Transition to Infrequent Access storage
#                 }
#             ],
#             'Expiration': {
#                 'Days': 365  # Delete objects after 365 days
#             },
#             'NoncurrentVersionExpiration': {
#                 'NoncurrentDays': 365  # Delete noncurrent versions of objects after 365 days
#             }
#         },
#         {
#             'ID': 'Archive-to-Glacier-after-60-days',
#             'Prefix': 'archive/',  # Apply the rule only to objects with 'archive/' prefix
#             'Status': 'Enabled',
#             'Transitions': [
#                 {
#                     'Days': 60,  # Transition to Glacier after 60 days
#                     'StorageClass': 'GLACIER'
#                 }
#             ]
#         }
#     ]
# }

# configureLifeCycleRules('pasta-bucket-0303',lifecyclePolicy)

# getLifeCycleRules('pasta-bucket-0303')

# enableVersioning('pasta-bucket-0303')

# enableLogging('pasta-bucket-0303',"log-bucket-0303" )

