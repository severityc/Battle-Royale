from Player import Player
from random import randint
from time import sleep

class Voldemort(Player):
  def __init__(self):
    Player.__init__(self, "Voldemort")
    self.moves.pop("attack")
    self.moves.pop("heal")
    self.moves["crucio"] = self.attack
    self.moves["regeneration"] = self.heal
    self.moves["killing curse"] = self.avadakedavra
  
  def avadakedavra(self, enemy):
    print("AVADA KEDAVRA!!")
    sleep(1)
    # half chance you hit enemy
    if randint(0, 1):
      self.attack(enemy, 50)
    # half chance you hit yourself
    else:
      print("Voldemort's attack rebounded!")
      self.attack(self, 50)
