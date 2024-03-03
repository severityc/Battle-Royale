from Player import Player

class Venom(Player):
  def __init__(self):
    Player.__init__(self, "Venom")
    
    self.moves["venom fang"] = self.venom_fang
    self.times_used = 3
    
  def venom_fang(self, enemy):
    if self.times_used > 0:
      self.attack(enemy, 40)
      self.times_used -= 1
      print(str(self.times_used) + " time(s) left to use this move")
    else:
      print("You can't use this power move anymore. Turn lost.")
  
