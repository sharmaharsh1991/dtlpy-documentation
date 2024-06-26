# sync aws s3 → platforma

### step 1: create a s3 storage that config with a lambda function:

**make sure that the function and the bucket in the same region**

* create a lambda:
    * go to aws lambda press create function

    * write your function name

    * Runtime choose python 3.6

    * in Permissions → Change default execution role → Create a new role from AWS policy templates

    * write your role name

    * in Policy templates choose :  Amazon S3 object read-only permissions

![lambda](https://i.imgur.com/XH5ZxcP.png)

* create s3 bucket:

    * go to aws S3 press create bucket

    * create the bucket with the default values

    * go to your bucket

    * go to Properties → Event notifications → Create event notification

    * write the event name

    * for Event types choose: All object create events, All object delete events

    * Destination - Lambda function → Choose from your Lambda functions → choose the function you build → SAVE

### step 2: build a sync dataset for your bucket

* [DOCS](https://dataloop.ai/docs/sdk-sync-storage?highlight=extrna)
* [CODE](sync_dataset.py)

### step 3: builds the code and the environment 
**use linux os**
* open a folder → open a terminal  
  ```
  sudo apt-get update
  ```   
  
*  create a virtaul venv ,activate it and install dtlpy package

  ```
   python3 -m venv env
   source env/bin/activate
   pip3 install dtlpy
   deactivate
  ``` 
  
* replace the numpy and pandas packages with numpy and pandas packages for aws  
[numpy, pandas for aws lambda](https://github.com/0xpetersatoshi/aws-lambda-py3.6-pandas-numpy)  
  
* add a file [CODE](lambda_function.py) to the same folder of all the packages     
  (env/lib/python3.X/site-packages)

* compress all the packages and code in one zip file

* upload this file to the s3 bucket 

* insert to the uploaded zip in aws S3
  
* copy his s3 URL  

* go to lambda 

* code → upload from → Amazon S3 location

* update the timeout of the lambda (default is 3 sec and it not enough) it have to be 15min >= timeout >= 1min  
configuration → General configuration → Edit → Timeout

![set code](https://i.imgur.com/mlqSUCd.png)

* It is recommended to connect the Lambda to a logger in order to track any errors

* to monitor your actions insert to lambda monitor 

![monitor](https://i.imgur.com/1Ce4xKm.png)