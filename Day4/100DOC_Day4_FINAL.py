#100DOC_Day4_FINAL.py
#Randomization - Python uses Mersenne Twister

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

#game images list for future reference
game_images = [rock, paper, scissors]
#user enters their choice
user_choice = int(input("What do you choose? 0 for R, 1 for P, or 2 for S? \n"))
#validating user didn't put a valid number in for game to work correctly
if user_choice >= 3 or user_choice < 0:
    print("Invalid choice, so you lose. ")
else:
    print(game_images[user_choice])
#computer takes their turn now
computer_choice = random.randint(0, 2)
print(game_images[computer_choice])
#game logic
if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose to rock...")
elif computer_choice > user_choice:
    print("You lose...")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("Draw...")


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][1])
