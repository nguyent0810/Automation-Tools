import requests

access_token = ""
url = f"https://graph.facebook.com/v15.0/me?fields=id%2Cname&access_token={access_token}"

response = requests. get(url)
print(response.text)