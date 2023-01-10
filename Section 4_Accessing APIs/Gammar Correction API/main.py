import requests
import json

access_token = ""
url = f"https://api.languagetoolplus.com/v2/check"

data = {
    'text': 'Tis is a nixe day!',
    'language': 'auto'
}
response = requests. post(url, data=data)
result = json.loads(response.text)
print(result['software'])