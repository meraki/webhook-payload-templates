import requests
import json


USER_ID = 'XXX'
CHANNEL_ACCESS_TOKEN = 'YYY'


url = 'https://api.line.me/v2/bot/message/push'
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {}'.format(CHANNEL_ACCESS_TOKEN)
}
payload = {
  'to': USER_ID,
  'messages': [
    {
      'type': 'text',
      'text': 'This is a test.'
    }
  ]
}

response = requests.request('POST', url, headers=headers, data=json.dumps(payload))

print(response.text)
