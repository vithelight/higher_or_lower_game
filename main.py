# Python base
from random import choice
from os import system
# Project base
from art import logo, vs
from resources import data
# Third party 
from termcolor import colored

# Info
  # - Compare two objects based on their Insta followers' count

# Todos
  # - functionality to read and compare two objects and return the result
  # - functionality to randomly get two objects from an array
  # - functionality to get user's guess and compare it with the result of two objects
  # - functionality to check if user's guess is true or not
  # - functionality to increment score if true else exit application


# Constants
NAME = 'name'
DESCRIPTION = 'description'
COUNTRY = 'country'
FOLLOWER_COUNT = 'follower_count'

# Get two random objects
def get_two_random_object(array):
  return choice(array), choice(array)

# Compare two objects
def compare_objects(a, b):
  return a if a['follower_count'] > b['follower_count'] else b




# Get user input and return accordingly
def get_user_input():
  guess = input('Who has more followers? Type \'A\' or \'B\': ').lower()
  if guess == 'a':
    return 1
  elif guess == 'b':
    return 2
  else:
    return 0
  
# Compare user input
def compare_user_input(user_input, winner):
  return True if user_input == winner else False

# Main function
def main():
  print(logo)
  score = 0
  while True:
    object_a, object_b = get_two_random_object(data)
    winner = compare_objects(object_a, object_b)
    objects = {
      0: 'Not valid',
      1: object_a,
      2: object_b
    }
    print('Compare {}: {}, a(n) {}, from {}'.format(colored('A', 'magenta'), colored(object_a[NAME], 'green'), colored(object_a[DESCRIPTION], 'blue'), colored(object_a[COUNTRY], 'light_yellow')))
    print(vs)
    print('Against {}: {}, a(n) {}, from {}'.format(colored('B', 'magenta'), colored(object_b[NAME], 'green'), colored(object_b[DESCRIPTION], 'blue'), colored(object_b[COUNTRY], 'light_yellow')))
    if compare_user_input(objects[get_user_input()], winner):
      score += 1
      system('clear')
      print(colored(f'\nYou\'re correct. Current Score: {score}', 'green'))
    else:
      system('clear')
      print(colored(f'\nSorry, that\'s wrong. Final score: {score}', 'red'))
      break
    

if __name__ == '__main__':
  main()