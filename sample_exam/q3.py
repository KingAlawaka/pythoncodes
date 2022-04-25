def readFile():
  fileDesc = open("counties.txt","r")
  lines = fileDesc.readlines()
  county = []
  population = []
  for l in lines:
    temp = l.strip().split(",")
    county.append(temp[0])
    population.append(int(temp[1]))
  return county,population

def countyStartsWith(list,letter):
  tempList = []
  for l in list:
    if l[0] == letter:
      tempList.append(l)
  return tempList

def countyWithLowestPopulation(county,population):
  indexOfTheLowest = population.index(min(population))
  return county[indexOfTheLowest]


county,population = readFile()
print(county)
print(population)

startWithList = countyStartsWith(county, "L")
print(startWithList)

countyName = countyWithLowestPopulation(county,population)
print(countyName)

