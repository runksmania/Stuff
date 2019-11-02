import random

dict_russian = {'А': 'a', 'Б': 'b', 'В': 'v', 'Г': 'g', 'Д': 'd', 'Е': 'ye', 'Ё': 'yo', 'Ж': 'zh', 'З': 'z', 'И': 'i', 'Й': 'y', 'К': 'k', 'Л': 'l', 'М': 'm', 'Н': 'n', 'О': 'o', 'П': 'p', 'P': 'r', 'С': 's', 'Т': 't', 'У': 'oo', 'Ф': 'f', 'Х': 'kh', 'Ц': 'ts', 'Ч': 'ch', 'Ш': 'sh', 'Щ': 'shch', 'Ъ': 'soft', 'Ы': 'y', 'Ь': 'hard', 'Э': 'e', 'Ю': 'yu', 'Я': 'ya'}

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
