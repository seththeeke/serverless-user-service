import boto3
import os
import uuid

# DB_TABLE_NAME is environment variable set to Users
def lambda_handler(event, context):
    username = event["Username"]

    print('Deleting DynamoDB record with username: ' + username)
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['DB_TABLE_NAME'])
    table.delete_item(
        Key={
            'Username': username
        }
    )
    
    return username