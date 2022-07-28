import json


def api_handler(event, context):
    first_name = event['querryStringParameters']['first_name']
    last_name = event['querryStringParameters']['last_name']

    app_response ={}
    app_response['message'] = 'Hello thser are the details for '+ first_name + '' + last_name
    app_response['profession'] = 'Developer'
    app_response['age'] =40


    responseObject ={}
    responseObject['statusCode'] = 200
    responseObject['headers' ] ={ }
    responseObject['headers']['Content-Type']= 'application/json'
    responseObject['body']= json.dumps(app_response)

    return responseObject