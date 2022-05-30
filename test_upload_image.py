import logging
import boto3
from botocore.exceptions import ClientError
import os

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)
    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def read_from_s3():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('supero')
    # Iterates through all the objects, doing the pagination for you. Each obj
    # is an ObjectSummary, so it doesn't contain the body. You'll need to call
    # get to get the whole body.
    for obj in bucket.objects.all():
        key = obj.key
        print(f'key = {key}')
        # body = obj.get()['Body'].read()
        # print(body)


def delete_file_by_name(bucket, key):
    s3 = boto3.resource('s3')
    s3.Object(bucket, key).delete()

if __name__ == '__main__':
    # upload_file(r'C:\Users\yassine_el_ghizi\Desktop\reduced_cats.sql', 'databasesupero', 'database_backups/supero_datalake-2022-05-3-14-43.sql')
    # upload_file(r'C:\Users\yassine_el_ghizi\Downloads\bestmark.png', 'supero', 'store/bestmark.png')
    # upload_file(r'C:\Users\yassine_el_ghizi\Downloads\electrobousfiha.png', 'supero', 'store/electrobousfiha.png')
    # upload_file(r'C:\Users\yassine_el_ghizi\Downloads\saligon.png', 'supero', 'store/saligon.png')
    # upload_file(r'C:\Users\yassine_el_ghizi\Downloads\cosmose.jpeg', 'supero', 'store/cosmose.jpeg')
    # upload_file(r'C:\Users\yassine_el_ghizi\Downloads\decathlon.png', 'supero', 'store/decathlon.png')
    upload_file(r'C:\Users\yassine_el_ghizi\Desktop\404.png', 'supero', 'images/404.png')
    # delete_file_by_name('databasesupero', 'database_backups/supero_datalake01.png')
    read_from_s3()