import requests
from bs4 import BeautifulSoup

r = requests.get('https://1000mostcommonwords.com/1000-most-common-italian-words/')
#r = requests.get('https://1000mostcommonwords.com/1000-most-common-russian-words/')
soup = BeautifulSoup(r.content, 'html5lib')

list_tds = [i.find_all('td') for i in soup.find_all('tr')]
output = []

for i in list_tds:
    output.append([i[1].get_text(), i[2].get_text()])

file_name = 'top1000ItalianWords.csv'
#file_name = 'top1000RussianWords.csv'

with open(file_name, mode='w', encoding='utf-8') as output_file:
    
    for i in output:
        print(','.join(i), file=output_file)