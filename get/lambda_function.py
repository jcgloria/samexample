import boto3
def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb')
    response = dynamodb.scan(TableName="tabledata")
    return list(map(lambda x: {"email": x['email']['S'], "name": x['name']['S'], "age": x['age']['S']}, response['Items']))
