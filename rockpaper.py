import random
Rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
Paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
Scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


images = [Rock, Paper, Scissors]
user = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors..: '))
if user >= 0 and user <= 2:
   print(images[user])

computer = random.randint(0,2)
print(f"Computer Choose..: ")
print(images[computer])

if user >= 3 or user < 0:
    print("You typed an Invalid number")
elif user == 0 and computer == 2:
    print("User WOn")

elif user == 1 and computer == 0:
    print("User Wins")
elif user == 1 and computer == 2:
    print("You Loose")
elif user == 2 and computer == 0:
    print("Computer Wins")
elif user == 1 and computer == 1:
    print("User Wins")
elif computer > user:
    print("You Loose")
elif computer == user:
    print("Its an Draw")




