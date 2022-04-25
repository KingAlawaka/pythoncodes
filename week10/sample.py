from Animal import Animal
from student import Student 

def main():
  dog = Animal("Dog", "Woof")
  dog.message()
  print(dog)

  st = Student("jack", 12)
  print(st)

main()