import json
import datetime


def Return(message, context):
    # log input message
    print('received message fromm Step Functions')
    print('mesage')
    
    # build response
    response = {}
    response['statusCode']= 200
    response['TransactionType'] = message['TransactionType']
    response['Timestamp'] = datetime.datetime.now().strftime('%Y')
    response['body']= 'New Return from Lambda Return function'
    
    # return response object
    return response