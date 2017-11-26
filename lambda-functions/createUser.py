import boto3
import os
import uuid

# DB_TABLE_NAME is environment variable set to Users
def lambda_handler(event, context):
    username = event["Username"]
    password = event["Password"]

    print('Generating new DynamoDB record, with username: ' + username)
    
    #Creating new record in DynamoDB table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['DB_TABLE_NAME'])
    table.put_item(
        Item={
            'Username' : username,
            'Password' : password,
        }
    )
    
    return username