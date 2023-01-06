import requests

# r = requests.get('https://newsapi.org/v2/everything?q=tesla&from=2022-12-06&sortBy=publishedAt&apiKey=33a53d27f2c443fb8acf4bbd1c585057')

# content = r.json()# articles = content['articles']

#
# for article in articles: #print('TITLE\n', article['title'], '\nDESCRIPTION\n', article['description'])

def get_news(topic, from_date, to_date, language = 'en', api_key = '33a53d27f2c443fb8acf4bbd1c585057'):
    url = f'https://newsapi.org/v2/everything?q={topic}&from={from_date}&to={to_date}&sortBy=popularity&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n'{ article['title']}, '\nDESCRIPTION\n', {article['description']}")
    return results

print(get_news("Tesla", from_date='2022-12-27', to_date='2022-12-28'))