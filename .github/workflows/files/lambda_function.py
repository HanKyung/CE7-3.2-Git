import json

def lambda_handler(event, context):
    incoming_msg = "good afternoon from Stephen, Alif, Dijay kumar, Lai Chua, Jun Jie!"
    return {
        'statusCode': 200,
        'body': json.dumps(incoming_msg)
    }
