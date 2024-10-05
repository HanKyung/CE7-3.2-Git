import json

def lambda_handler(event, context):
    incoming_msg = "Good Morning, Afternoon & Evening from Stephen, Alif, Jun Jie and Lai!"
    return {
        'statusCode': 200,
        'body': json.dumps(incoming_msg)
    }
