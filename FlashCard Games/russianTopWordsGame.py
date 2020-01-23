import random
from csv_processor_utf8 import process_csv

words_dict = {}

data = process_csv('../Dictionary/top1000RussianWords.csv')

for i in data:
    
    if i[1] != 'in English':
        words_dict[i[0]] = i[1]

user_input = ''
non_english_list = []
word_low_range = 0
word_high_range = 1000

for k,v in words_dict.items():

  non_english_list.append(k)

print('At anytime you can stop the game by typing quit')
print('Enter 1 to play top 100 words')
print('Enter 2 to play a random range of words')
print('Enter 3 to play all 1000 words')

user_input = input('Pick an option: ')

if user_input == '2':
    rand_amount = random.randint(101, 1000)
    rand_index = random.randint(0, 1000)
    coin_flip = random.randint(0,1)

    if coin_flip == 0:
        word_low_range = 0 if rand_index - rand_amount < 0 else rand_index - rand_amount
        word_high_range = word_low_range + 100 if word_low_range - rand_index < 100 else rand_index
        word_high_range = 999 if word_high_range > 999 else word_high_range

    else:
        word_high_range = 999 if rand_index + rand_amount > 999 else rand_index + rand_amount
        word_low_range = word_low_range - 100 if word_low_range + rand_index < 100 else rand_index
        word_low_range = 0 if word_high_range < 0 else word_low_range

elif user_input == '3':
    word_low_range = 0
    word_high_range = 999

else:
    word_low_range = 0
    word_high_range = 100


while user_input != 'quit':
  index = random.randint(word_low_range, word_high_range)
  word = non_english_list[index]

  user_input = input('What is this word in English ' + word + ':\n')

  if user_input != 'quit':

    if user_input == words_dict[word]:
      print('Correct.\n')

    else:
      print('Incorrect.')
      print('Correct answer: ' + words_dict[word] + '\n')
