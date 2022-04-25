def readFileAndList():
  file_desc = open("name.txt")
  #read all the lines at once
  lines = file_desc.readlines()
  print(lines)
  cleanList(lines)
  print(lines)
  file_desc.close()

def cleanList(listValues):
  for i in range(len(listValues)):
    listValues[i] = listValues[i].rstrip()

def readMultipleValuesToList():
  print("\n Reading multiple values \n")
  names = []
  ages = []
  file_desc = open("multivalue.txt")
  while True:
    line = file_desc.readline().rstrip()
    if line != "":
      values = line.split(",")
      print(values)
      names.append(values[0])
      ages.append(int(values[1]))
    else:
      break
  file_desc.close()
  return names, ages

def ListToFile(listvalues):
  file_desc = open("writeToFile.txt","w")
  for i in listvalues:
    print(i,file=file_desc)
    #file_desc.write(f"{i}\n")
  file_desc.close()
  
readFileAndList()

names, ages = readMultipleValuesToList()
print(names)
print(ages)
l = ["test", 123, "you","python"]
ListToFile(l)