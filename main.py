from bs4 import BeautifulSoup
import requests

url = "https://hackerwarehouse.com/product/bus-pirate/"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

result = requests.get(url, headers=headers)
soup = BeautifulSoup(result.text, "html.parser")
#print(soup)

try:
    nostock = soup.find('p', class_ = 'stock out-of-stock').text
    print(nostock)
except:
    print("In stock.")

try:
    cart = soup.find('button', class_='single_add_to_cart_button button alt').text
    print(cart)
except:
    print("Out of stock.")



