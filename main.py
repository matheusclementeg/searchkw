import urllib.request
from urllib.parse import quote
from bs4 import BeautifulSoup
import xlsxwriter

def extract_term(term):
    sanitized_term = quote(term)
    url = 'http://google.com/complete/search?output=toolbar&q={}'.format(sanitized_term)
    openurl = urllib.request.urlopen(url)
    mackup = openurl.read()
    soup = BeautifulSoup(mackup, 'html.parser')

    return soup

key = input("digita seu termo: ")
content = extract_term(key)

workbook = xlsxwriter.Workbook('teste.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})

header_col = 0
for col, link in enumerate(content.find_all('suggestion')):
    modulo = link.get('data')
    worksheet.write(0, header_col, modulo, bold)

    sub_content = extract_term(modulo)
    for row, sub_link in enumerate(sub_content.find_all('suggestion')):
        sub_modulo = sub_link.get('data')

        worksheet.write(row + 1, header_col, sub_modulo)

    header_col += 1

workbook.close()
