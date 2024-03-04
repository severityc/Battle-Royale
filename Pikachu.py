from random import randint
from Player import Player

# Pikachu class
class Pikachu(Player):
  def __init__(self):
    Player.__init__(self, "Pikachu")
    self.moves["thunder shock"] = self.thunder_shock

  # special move
  def thunder_shock(self, enemy):
    # strong attack
    damage = randint(40, 50)  
    self.attack(enemy, damage)
    # 50% chance of lowering own health
    if randint(0, 1):         
      self.health -= 10   
            
