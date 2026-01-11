import json
import boto3
import os
from decimal import Decimal

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('DYNAMODB_TABLE', 'cv-visitor-counter')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    """
    Lambda function to increment visitor counter in DynamoDB and return the new count.
    """
    try:
        # Atomic increment of the visitor count
        response = table.update_item(
            Key={
                'id': 'visitors'
            },
            UpdateExpression='ADD #count :inc',
            ExpressionAttributeNames={
                '#count': 'count'
            },
            ExpressionAttributeValues={
                ':inc': 1
            },
            ReturnValues='UPDATED_NEW'
        )
        
        # Get the new count, handle Decimal to float/int conversion for JSON serialization
        new_count = response['Attributes']['count']
        if isinstance(new_count, Decimal):
            new_count = int(new_count)
            
        body = {
            'count': new_count
        }
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': 'https://cv.aws10.dcoletasix2a.cat',
                'Access-Control-Allow-Methods': 'GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps(body)
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': 'https://cv.aws10.dcoletasix2a.cat',
                'Access-Control-Allow-Methods': 'GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'error': 'Could not increment visitor count'})
        }
