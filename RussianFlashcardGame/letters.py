import random

dict_russian = {'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v', 'Г': 'G', 'г': 'g', 'Д': 'D', 'д': 'd', 'Е': 'Ye', 'е': 'ye', 'Ё': 'Yo', 'ё': 'yo', 'Ж': 'Zh', 'ж': 'zh', 'З': 'Z', 'з': 'z', 'И': 'I', 'и': 'i', 'Й': 'Y', 'й': 'y', 'К': 'K', 'к': 'k', 'Л': 'L', 'л': 'l', 'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p', 'P': 'R', 'p': 'r', 'С': 'S', 'с': 's', 'Т':'T', 'т': 't', 'У': 'Oo', 'у': 'oo', 'Ф': 'F', 'ф': 'f', 'Х': 'kh', 'х': 'kh', 'Ц': 'Ts', 'ц': 'ts', 'Ч': 'Ch', 'ч': 'ch', 'Ш': 'Sh', 'ш': 'sh', 'Щ': 'Shch', 'щ': 'shch', 'Ъ': 'soft', 'ъ': 'soft', 'Ы': 'Y', 'ы': 'y', 'Ь': 'hard', 'ь': 'hard', 'Э': 'E', 'э': 'e', 'Ю': 'Yu', 'ю': 'yu', 'Я': 'Ya', 'я': 'ya'}
user_input = ''
russian_list = []

for k,v in dict_russian.items():

  russian_list.append(k)

while user_input != 'quit':
  index = random.randint(0, len(russian_list))
  letter = russian_list[index]

  user_input = input('What is this letter ' + letter + ':\n')

  if user_input != 'quit':

    if user_input == dict_russian[letter]:
      print('Correct.\n')
    else:
      print('Incorrect.')
      print('Correct answer: ' + dict_russian[letter] + '\n')
