### 
# Authtor: Nguyen Manh Dung
# Roll pair of dices and decide who is winner
###

from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(raw_input("Enter your guess: "))
  return user_guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "Max value you can guess: " + str(max_val)
  sleep(1)
  user_guess = get_user_guess()
  if user_guess > max_val:
    print "You are not allowed to guess a value greater than " + str(max_val)
    return
  else:
    print "Rolling..."
    sleep(2)
    print "First roll: %d" % first_roll
    sleep(1)
    print "Second roll: %d" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print "Total roll: %d" % total_roll
    print "Resul..."
    sleep(1)
    if user_guess > total_roll:
      print "You won"
    else:
      print "Sadly, you lost"
roll_dice(6)
