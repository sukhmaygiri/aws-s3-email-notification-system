# AWS Serverless File Upload Notification System

## Project Overview

This project demonstrates an event-driven serverless architecture on AWS.

Whenever a file is uploaded to an Amazon S3 bucket, an AWS Lambda function is automatically triggered. The Lambda function publishes a message to an Amazon SNS topic, which sends an email notification to subscribed users.

## Architecture

User Uploads File → S3 Bucket → Lambda Function → SNS Topic → Email Notification

## AWS Services Used

- Amazon S3
- AWS Lambda
- Amazon SNS
- AWS IAM
- Amazon CloudWatch

## Workflow

1. User uploads a file to the S3 bucket.
2. S3 generates an Object Created event.
3. Lambda function is triggered automatically.
4. Lambda extracts the bucket name and file name.
5. Lambda publishes a message to SNS.
6. SNS sends an email notification to subscribers.

## Project Structure

```
aws-s3-email-notification-project/
│
├── lambda_function.py
├── README.md
├── architecture.png
└── screenshots/
```

## Lambda Function

The Lambda function performs the following tasks:

- Receives S3 upload event
- Extracts file information
- Publishes notification to SNS topic
- Sends email notification

## Sample Email

Subject:
New File Uploaded

Message:
File sample.csv uploaded to bucket sukhmay-upload-bucket

## Skills Demonstrated

- Serverless Computing
- Event-Driven Architecture
- AWS Cloud Services
- IAM Permissions
- SNS Notifications
- CloudWatch Monitoring

## Future Enhancements

- Store upload metadata in DynamoDB
- Send notifications to multiple users
- Add file size and upload time in email
- Integrate with SQS
- Create monitoring dashboard

## Author

Sukhmay Giri
