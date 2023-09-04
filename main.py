from bs4 import BeautifulSoup
import requests

url = "https://hackerwarehouse.com/product/bus-pirate/"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

result = requests.get(url, headers=headers)
soup = BeautifulSoup(result.text, "html.parser")
#print(soup)

# create a new file
try:
    newfile = open("result.txt", "x")
except:
    print("File exists.")

# parse soup and write result to file
newfile = open("result.txt", "w")

try:
    nostock = soup.find('p', class_ = 'stock out-of-stock').text
    newfile.write(nostock)
    newfile.write("\n")
except:
    newfile.write("In stock.")
    newfile.write("\n")
try:
    cart = soup.find('button', class_='single_add_to_cart_button button alt').text
    newfile.write(cart)
except:
    newfile.write("Out of stock.")
newfile.close()

newfile = open("result.txt", "r")
print(newfile.read())
newfile.close()



