# serverless-user-service
First Experience with AWS Lambda

This is a sample web application that interacts with AWS API Gateway that triggers Lambda functions to perform CRUD operations on a dynamo db table

The architecture involves a static hosted website on S3 at http://seth-theeke-dynamo-db-website.s3-website-us-east-1.amazonaws.com/ and the web application makes HTTP calls to a configured API Gateway for managing users. When the API Gateway is hit, it triggers a corresponding lambda function. Each lambda function interacts with a dynamo db table to Read, Write, Update, and Delete from the Dynamo Db table
