from random import randint

# super class, parent class
class Player:
  def __init__(self, name):
    self.name = name
    self.health = 100
    
    # create dictionary of moves
    self.moves = {}
    
    # add attack move
    self.moves["attack"] = self.attack
    
    # add heal move
    self.moves["heal"] = self.heal
    
  # status function prints player stats
  def status(self):
    print(self.name + " health: " + str(self.health))
    
  # show moves
  def show_moves(self):
    print(self.name + " 's moves: ")
    
    # print list of keys in moves dictionary
    for moveName in self.moves.keys():
      print(moveName)
      
  # attack method lowers enemy's health by random amount
  def attack(self, enemy, damage=-1):
    if damage == -1:
      damage = randint(20, 40)
      
    enemy.health -= damage
    print(self.name + " did " + str(damage) + " damage to " + enemy.name)
  
  # heal method: heal player by random amount (amt)
  def heal(self, enemy):
    # get random healing amount
    healAmt = randint(25, 45)
    self.health += healAmt
    
    print(self.name + " healed self by: " + str(healAmt))
