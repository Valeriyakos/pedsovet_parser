import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

url = 'https://pedsovet.org/'

try:
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='cards-unt-item')
    
    data = []
    for i in items:
        title_block = i.find('div', class_='cards-unt-item__title')
        if not title_block:
            continue
            
        link = title_block.find('a')
        if not link:
            continue
            
        data.append({
            'name': link.get_text(strip=True),
            'link': urljoin(url, link.get('href'))
        })
    
except requests.RequestException as e:
    print(f"Ошибка загрузки: {e}")
    data = []

# Вывод результатов
print(f"Найдено: {len(data)}\n")

for num, item in enumerate(data, 1):
    print(f"{num}. {item['name']}")
    print(f"   {item['link']}\n")

# Сохранение в JSON
with open('articles.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)