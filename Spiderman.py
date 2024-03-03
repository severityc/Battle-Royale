from Player import Player

# spiderman class (child of Player)
class Spiderman(Player):
  
  def __init__(self):
    # use init in parent class
    Player.__init__(self, "Spiderman")
    
    # add new move to spiderman dictionary
    self.moves["web throw"] = self.web_throw
    self.times_used = 3
  
  def web_throw(self, enemy):
    if self.times_used > 0:
      self.attack(enemy, 40)
      self.times_used -= 1
      print(str(self.times_used) + " time(s) left to use this move.")
    else:
      print("You can't use this move anymore. Turn lost.")
    
