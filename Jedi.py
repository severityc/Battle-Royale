from Player import Player

# Jedi class
class Jedi(Player):
  def __init__(self):
    Player.__init__(self, "Jedi")
    self.energy = 1
    # track use of special move
    self.specialmove = 3
        
    # remove old attack name
    self.moves.pop("attack")
    # rename basic attack move
    self.moves["lightsaber slash"] = self.attack
    self.moves["force whirlwind"] = self.force_attack
    self.moves["battlemind"] = self.force_mind
        
        
  # special support move (can only be used if energy is not too high)
  def force_mind(self, enemy):
    # increase energy (attack/heal strength)
    self.energy += 0.2
    print("Meditation increases the concentration of " + self.name)
    print(self.name + " has increased energy.")
    # if energy gets too high...
    if self.energy >= 1.8:                
      # remove from dictionary of possible moves
      self.moves.pop("battlemind")

  # special attack move (limited to 2 uses)
  def force_attack(self, enemy):
    self.attack(enemy, (self.energy * 60))
    # subtract 1 use of specialmove
    self.specialmove -= 1                 
    if self.specialmove > 0:
      print(str(self.specialmove) + " times left to use this move.")
    else:          
      # if 0 specialmoves left
      # remove from dict of possible moves
      self.moves.pop("force whirlwind")
      
      
      
      
      
