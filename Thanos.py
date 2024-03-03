from random import uniform
from Player import Player

class Thanos(Player):
  def __init__(self):
    Player.__init__(self, "Thanos")
    self.moves.pop("attack")
    self.moves["smash"] = self.attack
    self.moves["Thanos Snap"] = self.finger_snap

  def finger_snap(self, enemy):
    damage = round(enemy.health / 2)
    # reduces enemy's health by half
    self.attack(enemy, damage)
    n = uniform(0, self.health/2)
    # also randomly injures himself
    self.attack(self, round(n))
