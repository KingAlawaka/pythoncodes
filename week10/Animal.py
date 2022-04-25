class Animal:
  def __init__(self,name,sound):
    self.name = name
    self.sound = sound

  def message(self):
    print(f"Animal {self.name}")

  def __str__(self):
    return f"Animal {self.name} sounds like this {self.sound}"
