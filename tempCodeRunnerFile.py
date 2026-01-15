import requests
from bs4 import BeautifulSoup
import json

accept = 'html/text'
usr_ag = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'

headers = {'Accept': accept, 'User-Agent': usr_ag}
allq = []
page = 1
while True:
    URL = f'https://quotes.toscrape.com/page/{page}/'

    response = requests.get(URL, headers = headers )

    if response.status_code != 200:
        print(f'Error: {response.status_code}')
        print(response.text[500])
    else:
        print('Ok')
    print('-' * 66)

    html = response.text

    soup = BeautifulSoup(html, 'lxml')


    res = []
    quotes = soup.find_all('div', class_='quote')
    if not quotes:
        break
    for q in quotes:
        text = q.find('span', class_='text').text
        author = q.find('small', class_='author').text
        res.append({'quote': text, 'author': author})
    for i in res:
        allq.append({'author': author, 'quote': text})
    page += 1
        
with open('quotes.json', 'w', encoding='utf-8') as f:
    json.dump(allq, f, ensure_ascii=False, indent=2)
print(f'Сохранено цитат:{len(allq)}')
