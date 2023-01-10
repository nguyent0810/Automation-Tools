import requests

def get_weather(city, units='metric', api_key=''):
    url = ''
    r = requests.get(url)
    content = r.json()
    with open('data.txt', 'a') as file:
        for dicty in content['list']:
            file.write(f"{dicty['dx_txt']}, {dicty['weather'][0]['description']}\n")
    return content

print(get_weather())