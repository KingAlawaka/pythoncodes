class Student:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def message(self):
    print(f"message {self.name}")


  #builting python function to get address of the object
  def __str__(self):
    return f"name {self.name} and age {self.age}"
  

def main():
  s1 = Student("Jack",12)
  print(s1)
  print(s1.__dict__)
  s1.message()

#main()
if __name__ == '__main__':
  main()
