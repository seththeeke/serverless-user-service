import boto3
import os
from boto3.dynamodb.conditions import Key, Attr

# Returns all users
# DB_TABLE_NAME is environment variable set to Users
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['DB_TABLE_NAME'])
    items = table.scan()
    return items["Items"]