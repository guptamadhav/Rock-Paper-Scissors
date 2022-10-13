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
game_images=[rock,paper,scissors]
num=int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors "))
import random
i=random.randint(0,2)
if num>=3 or num<0:
  print('You typed an invalid number, you lose!!')
else:
  print(game_images[num])
  print('Computer chose:')
  print(game_images[i])
  if num==i:
    print('Draw')
  elif num==0 and i==1:
    print('You lose')
  elif num==0 and i==2:
    print('You won')
  elif num==1 and i==0:
    print('You won')
  elif num==1 and i==2:
    print('You lose')
  elif num==2 and i==0:
    print('You lose')
  elif num==2 and i==1:
    print('You won')


