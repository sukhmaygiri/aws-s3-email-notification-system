import boto3

sns = boto3.client('sns')

TOPIC_ARN = 'arn:aws:sns:ap-south-2:183192605590:s3-upload-topic'

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    filename = event['Records'][0]['s3']['object']['key']

    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject='New File Uploaded',
        Message=f'File {filename} uploaded to bucket {bucket}'
    )

    return {
        'statusCode': 200
    }
