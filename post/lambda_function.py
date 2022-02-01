import boto3
import json
def lambda_handler(event, context):
    request = json.loads(event['body'])
    dynamodb = boto3.client("dynamodb")
    return dynamodb.put_item(TableName="tabledata", Item={"email": {"S": request['email']}, "name": {"S": request['name']},"name": {"S": request['name']}, "age": {"S": request['age']},} )
    
