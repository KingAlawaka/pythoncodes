class Paint:
  def __init__(self,manufacture,colour,cost,size):
    self.manufacture = manufacture
    self.colour = colour
    self.cost = cost
    self.size = size

  def getCost(self):
    return self.cost
  
  def __str__(self):
    return f"Paint colour {self.colour} manufactured by {self.manufacture}, tin of {self.size} liters will cost {self.cost}"