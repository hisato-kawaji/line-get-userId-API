import json
import urllib.request


def hello(event, context):
    base_url = 'https://api.line.me'
    headers = {
        'Authorization': 'Bearer ' + '{access_token}',
        'Content-Type': 'application/json',
    }

    body = {
        "result": "result",
        "input": event,
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    k = json.loads(event['body'])
    t = k['events'].pop()
    message = 'あなたのIDは\n' + t['source']['userId'] + '\nです'
    post_data = {
        'to': t['source']['userId'],
        'messages': [
            {
                'type': 'text',
                'text': message
            }
        ]
    }
    if t['message']['text'] == 'ID':
        req = urllib.request.Request( base_url + '/v2/bot/message/push', json.dumps(post_data).encode(), headers)
        with urllib.request.urlopen(req) as res:
            k = res.read()
    return response
