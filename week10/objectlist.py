from Animal import Animal

def main():
  dog = Animal("Dog", "Woof")
  cat = Animal("Cat", "meow")
  objectList = []
  objectList.append(dog)
  objectList.append(cat)

  objectList[0].message()
  print(objectList[1])

main()