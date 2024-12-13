import sys
import json
import logging

import boto3

logger = logging.getLogger(__name__)
lambda_client = boto3.client('lambda')

def invoke_the_thing(function_name, the_data):
    payload_json = json.dumps(the_data)

    try:
        response = lambda_client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',  # 'Event' for async invocation
            Payload=payload_json
        )

        print(f'Status code: {response["StatusCode"]}')

        if 'Payload' in response:
            payload = response['Payload'].read().decode('utf-8')
            print(f'Returned payload: {payload} {type(payload)=}')
    except Exception as wtf:
        logger.error(f'{wtf}', exc_info=True)

if __name__ == '__main__':
    f = sys.argv[1]
    data_file_name = sys.argv[2]

    tmp = None
    with open(data_file_name, 'r') as stuff:
        tmp = stuff.read()
        print(tmp)

    print(type(tmp))

