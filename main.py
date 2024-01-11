import random
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

chose = int(input("What do you chose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

print("User's chose:")
if chose == 0:
  print(rock)
if chose == 1:
  print(paper)
if chose == 2:
  print(scissors)

print("Computer chose:")
s = random.randint(0,2)

if s == 0:
  print(rock)
if s == 1:
  print(paper)
if s == 2:
  print(scissors)

if chose == s:
  print("Draw")
if chose == 0 and s == 1:
  print("Computer wins")
if chose == 1 and s == 0:
  print("You win")
if chose == 0 and s == 2:
  print("You win")
if chose == 2 and s == 0:
  print("Computer win")
if chose == 1 and s == 2:
  print("Computer win")
if chose == 2 and s == 1:
  print("You win")
