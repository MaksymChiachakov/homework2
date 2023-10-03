import requests, json
from bs4 import BeautifulSoup

# Сторінка куди надсилаємо запит
url = 'https://scrapingclub.com/exercise/list_basic_detail/94766-A/'

# Виконуємо запит до сайту, та записуємо результат
response = requests.get(url)

# Отримуємо так званий 'суп'
soup = BeautifulSoup(response.text, 'lxml')
# Результат
prices = soup.find_all('h4', class_='my-4 card-price')

products = soup.find_all('h3', class_='card-title')

some_data = list()
for i in range(len(prices)):
    for product in range(len(products)):
        some_data.append(products[product].text)
    some_data.append(prices[i].text)
    
print(some_data)

with open('result.json', 'w', encoding='utf8') as file:
    json.dump(some_data, file)

