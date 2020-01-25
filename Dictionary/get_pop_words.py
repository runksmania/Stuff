import requests
from heapq import heappop, heappush
from bs4 import BeautifulSoup

r = requests.get('https://1000mostcommonwords.com/1000-most-common-italian-words/')
#r = requests.get('https://1000mostcommonwords.com/1000-most-common-russian-words/')
soup = BeautifulSoup(r.content, 'html5lib')

list_tds = [i.find_all('td') for i in soup.find_all('tr')]
output = []

word_dict = {}

for i in list_tds:

    num = i[0].get_text()
    non_english_word = i[1].get_text()
    english_word = i[2].get_text()

    if num != 'Number':
        
        if non_english_word not in word_dict:
            word_dict[non_english_word] = [num, [english_word]]
        else:
            word_dict[non_english_word][1].append(english_word)

for k,v in word_dict.items():

    english_words = v[1][0]

    if len(v[1]) > 1:
        english_words = "\"" + ','.join(v[1]) + "\""

    heappush(output, (int(v[0]), k, english_words))

file_name = 'top1000ItalianWords.csv'
#file_name = './top1000RussianWords.csv'

with open(file_name, mode='w', encoding='utf-8') as output_file:
    print(','.join(['Number', 'Word', 'English Word(s)']), file=output_file)

    for i in range(len(output)):
        top = heappop(output)
        num = str(top[0]) + ','
        print(num + ','.join(top[1:]), file=output_file)