import requests, json
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

prices = soup.find_all('div', class_='p-4', limit=10)


my_list = []
for price in range(len(prices)):
    my_list.append(prices[price].text)


cleaned_product_list = [item.replace('\n', '') for item in my_list]

split_products = [item.split('$') for item in cleaned_product_list]

for product in split_products:
    print(f'Назва: {product[0]}.', f" Ціна: {product[1]}$")