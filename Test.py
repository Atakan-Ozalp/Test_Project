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

#Write your code below this line 👇
import random

game_images = [rock, paper, scissors]
Human = int(input("What do you choose? \n 0 for Rock, \n 1 for Paper, \n 2 for Scissors?\n"))
if Human >= 3 or Human < 0:
  print("You typed an invalid number, you lose!")
else:
  print("You chose")
  print(game_images[Human])
  Computer = random.randint(0, 2)
  print(f"Computer chose")
  print(game_images[Computer])

  if Human == 0 and Computer == 2:
    print("You win")
  elif Computer == 0 and Human == 2:
    print("You lose")
  elif Computer > Human:
    print("You lose")
  elif Human > Computer:
    print("You win")
  elif Computer == Human:
    print("It's a draw")
  else:
    print("You typed an invalid number, you lose")
