import json

def group_02_lambda_new(event, context):
    incoming_msg = "good afternoon from Stephen, Alif, Dijay kumar, Lai Chua, Jun Jie!"
    return {
        'statusCode': 200,
        'body': json.dumps(incoming_msg)
    }
