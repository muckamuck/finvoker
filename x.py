import sys
import json

import boto3

# Initialize the Lambda client
lambda_client = boto3.client('lambda')

def invoke_the_thing(function_name, the_data):
    payload = {
        'key1': 'value1',
        'key2': 'value2'
    }

    payload_json = json.dumps(payload)

    try:
        # Invoke the Lambda function
        response = lambda_client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',  # 'Event' for async invocation
            Payload=payload_json
        )

        # Print the status code of the invocation
        print(f'Status code: {response["StatusCode"]}')

        # Optionally, you can print the returned payload
        if 'Payload' in response:
            payload = response['Payload'].read().decode('utf-8')

            print(f'Returned payload: {payload} {type(payload)=}')

    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    f = sys.argv[1]
    data_file_name = sys.argv[2]

    tmp = None
    with open(data_file_name, 'r') as stuff:
        tmp = stuff.read()
        print(tmp)

    print(type(tmp))
