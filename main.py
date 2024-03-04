import random, time
from os import system

from helper import *
from Player import Player
from Spiderman import Spiderman
from Pikachu import Pikachu
from Elsa import Elsa
from Jedi import Jedi
from Voldemort import Voldemort
from Thanos import Thanos
from Venom import Venom

def createCharacter(name, answer):
  if answer == "spiderman":
    user = Spiderman()
    print(name + " picked Spiderman")
  elif answer == "pikachu":
    user = Pikachu()
    print(name + " picked Pikachu")
  elif answer == "elsa":
    user = Elsa()
    print(name + " picked Elsa")
  elif answer == "jedi":
    user = Jedi()
    print(name + " picked Jedi")
  elif answer == "voldemort":
    user = Voldemort()
    print(name + " picked Voldemort")
  elif answer == "thanos":
    user = Thanos()
    print(name + " picked Thanos")
  elif answer == "venom":
    user = Venom()
    print(name + " picked Venom")
  
  return user

playAgainOptions = ["y", "yes", "yup", "sure", "ye", "yee"]
playAgain = "y"
userScore = 0
botScore = 0

while playAgain in playAgainOptions:
  playerList = ["spiderman", "pikachu", "elsa", "jedi", "voldemort", "thanos", "venom"]
  
  print("Ready for battle!")
  print("")
  print("Who do you want to play as?")
  for player in playerList:
    print(player)
    
  answer = input(">")
  while answer not in playerList:
    print("Please enter valid player.")
    answer = input(">")
  
  user = createCharacter("user", answer)
  user.status()
  
  print("")
  botChoice = random.choice(playerList)
  bot = createCharacter("bot", botChoice)
  bot.status()
  
  while user.health > 0 and bot.health > 0:
    # ask user to choose and do move
    user_move(user, bot)
    
    # if bot is still alive, it moves
    if bot.health > 0:
      bot_move(user, bot)
  
  if user.health <= 0:
    print(bot.name + " wins!!!")
    botScore += 1
  else:
    print("You win!!")
    userScore += 1
  
  
  print("Current user score: " + str(userScore))
  print("Current bot score: " + str(botScore))
  print("")
  sleep(2)
  playAgain = input("Would you like to play again?")
  playAgain = playAgain.lower().strip()
  
  # clears the screen
  system("clear")

print("Game over!!")
print("Final user score: " + str(userScore))
print("Final bot score: " + str(botScore))
print("")

if userScore > botScore:
  print("You beat the machine!")
elif userScore == botScore:
  print("You both tied!")
else:
  print("The machine is victorious!")
