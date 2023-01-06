import requests


def get_news(country, api_key = '33a53d27f2c443fb8acf4bbd1c585057'):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n'{ article['title']}, '\nDESCRIPTION\n', {article['description']}")
    return results

print(get_news('USA'))