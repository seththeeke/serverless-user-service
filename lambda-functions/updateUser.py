import boto3
import os
import uuid

# DB_TABLE_NAME is environment variable set to Users
def lambda_handler(event, context):
    username = event["Username"]
    password = event["Password"]

    print('Updating DynamoDB record with username: ' + username)
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['DB_TABLE_NAME'])
    table.update_item(
        Key={
            'Username': username,
        },
        UpdateExpression='SET Password = :val1',
        ExpressionAttributeValues={
            ':val1': password
        }
    )
    
    return username