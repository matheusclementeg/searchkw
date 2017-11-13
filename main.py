import urllib.request
from bs4 import BeautifulSoup
import xlsxwriter

key = input("digita seu termo")
key = ('%20').join(key.split(' '))
url = 'http://google.com/complete/search?output=toolbar&q={}'.format(key)
openurl = urllib.request.urlopen(url)
mackup = openurl.read()
soup = BeautifulSoup(mackup, 'html.parser')

workbook = xlsxwriter.Workbook('teste.xlsx')
worksheet = workbook.add_worksheet()

planilha = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13']
row = 0
for link in soup.find_all('suggestion'):
    modulo = link.get('data')
    worksheet.write(row, 0, modulo) # 0 é a coluna (ou seja, A)
    row += 1

workbook.close()
