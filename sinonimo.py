import urllib.request
from bs4 import BeautifulSoup

key = input("Informe a palavra: ")
kw = ("%20").join(key.split(' '))
url = 'https://www.sinonimos.com.br/'.format(kw)
openurl = urllib.request.urlopen(url)
mackup = openurl.read()
soup = BeautifulSoup(mackup, 'html.parser')
for link in soup.find_all('p', {"class": "sinonimos"}):
    print(link.get('a'))
