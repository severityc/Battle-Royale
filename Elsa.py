from Player import Player

# Elsa class
class Elsa(Player):
  def __init__(self):
    Player.__init__(self, "Elsa")
    self.moves["ice blast"] = self.ice_blast

  def ice_blast(self, enemy):
    self.attack(enemy, 30)
    # heals herself
    self.health += 10                
