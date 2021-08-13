import json
import requests
import random

def lambda_handler(event, context):
    # TODO implement
	url = 'https://api.line.me/v2/bot/message/push'
	msg = ['カーボンかけろー!', '薬を飲みましょう', '血圧を測ろう']
	msg = random.choice(msg)
	data = {}
	data['to'] = '{lineグループID}'
	data['messages'] =[{"type": "text", "text": msg}]
	headers={'Content-Type': 'application/json'}
	headers['Authorization'] = 'Bearer {アクセストークン}'
	response = requests.post(url, json=data, headers=headers)
	return {'statusCode': 200, 'body': json.dumps(response.json())}