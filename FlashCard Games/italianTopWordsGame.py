import random
from csv_processor_utf8 import process_csv

words_dict = {}

data = process_csv('../Dictionary/top1000ItalianWords.csv')

for i in data:
    
    if i[0] != 'Number':
      word_list = i[2].split(',')
      words_dict[i[1]] = word_list

user_input = ''
non_english_list = []
word_low_range = 0
word_high_range = len(data)

for k,v in words_dict.items():

  non_english_list.append(k)

print('At anytime you can stop the game by typing quit')
print('Enter 1 to play top 100 words')
print('Enter 2 to play a random range of words')
print('Enter 3 to play all 1000 words')

user_input = input('Pick an option: ')

if user_input == '2':
    rand_amount = random.randint(101, len(data))
    rand_index = random.randint(0, len(data))
    coin_flip = random.randint(0,1)

    if coin_flip == 0:
        word_low_range = 0 if rand_index - rand_amount < 0 else rand_index - rand_amount
        word_high_range = word_low_range + 100 if word_low_range - rand_index < 100 else rand_index
        word_high_range = len(data) - 1 if word_high_range > len(data) - 1 else word_high_range

    else:
        word_high_range = len(data) - 1 if rand_index + rand_amount > len(data) - 1 else rand_index + rand_amount
        word_low_range = word_low_range - 100 if word_low_range + rand_index < 100 else rand_index
        word_low_range = 0 if word_high_range < 0 else word_low_range

elif user_input == '3':
    word_low_range = 0
    word_high_range = len(data) - 1

else:
    word_low_range = 0
    word_high_range = 100


while user_input != 'quit':
  index = random.randint(word_low_range, word_high_range)
  word = non_english_list[index]

  user_input = input('What is this word in English ' + '\x1B[3m' + word + '\x1B[23m' + ':\n')

  if user_input != 'quit':

    if user_input in words_dict[word]:
      print('Correct.')

      if len(words_dict[word]) > 1:
        print('All correct answers: ' + ', '.join(words_dict[word]))

      print()

    else:
      print('Incorrect.')\

      if len(words_dict[word]) > 1:
        print('Correct answers: ' + ', '.join(words_dict[word]))
      else:
        print('Correct answer: ' + ''.join(words_dict[word]))
      
      print()
