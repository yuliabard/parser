from urllib.request import urlopen
from bs4 import BeautifulSoup

url=input('Введите адрес:')
html_doc = urlopen(url).read()
soup = BeautifulSoup(html_doc,'html.parser')

print('\nИзображения:')
for img in soup.find_all('img'):
    print(img.get('src'))

print('\nСсылки:')
for links in soup.find_all('a'):
    print (links.get('href'))