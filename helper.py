from random import choice
from time import sleep

# status function displays stats of everyone
def status(user, bot):
    print("")
    print("-" * 40)
    user.status()
    bot.status()
    print("-" * 40)

# user_move(): asks user to choose move, then use move against bot
def user_move(user, bot):
    print("")
    print("Choose a move : ")
    
    # print keys of user moves
    for move in user.moves:
        print(move)
        
    answer = input(">")
    
    # repeat till user enters a valid move
    while answer not in user.moves:
        print("Invalid command. Enter move again.")
        answer = input(">")
        
    print(user.name + " uses: " + answer)
    
    # look up move in dictionary w/ key
    move = user.moves[answer]
    # use move on bot
    move(bot)
    
    sleep(1)
    status(user, bot)
    sleep(1)

# bot_move(): bot randomly chooses move and uses against user  
def bot_move(user, bot):
    print("")
    print("Computer's turn...")
    sleep(1)
    
    if bot.health <= 20:
        move_name = "heal"
    else:
        # randomly choose move for bot
        move_name = choice(list(bot.moves.keys()))
    
    # look up move in dictionary
    move = bot.moves[move_name]
    print(bot.name + " uses: " + move_name)
    move(user)
    
    sleep(1)
    status(user, bot)
    sleep(1)
