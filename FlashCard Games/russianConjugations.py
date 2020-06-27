import random

#Keys are all the endings for russian words.
#Values are lists which have what conjugation group followed by a dictionaries containing the pronouns and how to conjugate for that pronoun.
endings_dict = {
    'aTЬ' : ['1', {'Я' : 'you', 'TЫ' : 'yesh', 'OH' : 'yet', 'OHA' : 'yet', 'MЫ' : 'yem', 'BЫ' : 'yetye', 'OHИ' : 'yout'}],
    'ять' : ['1', {'Я' : 'you', 'TЫ' : 'yesh', 'OH' : 'yet', 'OHA' : 'yet', 'MЫ' : 'yem', 'BЫ' : 'yetye', 'OHИ' : 'yout'}],
    'еть' : ['1', {'Я' : 'you', 'TЫ' : 'yesh', 'OH' : 'yet', 'OHA' : 'yet', 'MЫ' : 'yem', 'BЫ' : 'yetye', 'OHИ' : 'yout'}],
    'овать' : ['1', {'Я' : 'you', 'TЫ' : 'yesh', 'OH' : 'yet', 'OHA' : 'yet', 'MЫ' : 'yem', 'BЫ' : 'yetye', 'OHИ' : 'yout'}],
    'нуть' : ['1', {'Я' : 'you', 'TЫ' : 'yesh', 'OH' : 'yet', 'OHA' : 'yet', 'MЫ' : 'yem', 'BЫ' : 'yetye', 'OHИ' : 'yout'}],
    'ить' : ['2', {'Я' : 'you', 'TЫ' : 'eesh', 'OH' : 'eat', 'OHA' : 'eat', 'MЫ' : 'eem', 'BЫ' : 'eetye', 'OHИ' : 'yat'}]
}

user_input = ''
russian_list = []
pronouns = ['Я', 'TЫ', 'OH', 'OHA', 'MЫ', 'BЫ', 'OHИ']

for k,v in endings_dict.items():

  russian_list.append(k)

while user_input != 'quit':
  index = random.randint(0, len(russian_list) - 1)
  pronoun = pronouns[random.randint(0, len(pronouns) - 1)]
  ending = russian_list[index]

  user_input = input('What is the conjugation group for the the verb ending ' + ending + ':\n')

  if user_input == 'quit':
      break
  else:
    if user_input == endings_dict[ending][0]:
      print('Correct.\n')
    else:
      print('Incorrect.')
      print('Correct answer: ' + endings_dict[ending][0] + '\n')

  user_input = input('What is the conjugation ending for the pronoun ' + pronoun + ' and the verb ending ' + ending + ':\n')

  if user_input != 'quit':

    if user_input == endings_dict[ending][1][pronoun]:
      print('Correct.\n')
    else:
      print('Incorrect.')
      print('Correct answer: ' + endings_dict[ending][1][pronoun] + '\n')