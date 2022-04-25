def noReturn():
  print("No return")

def oneRetValue():
  return "one value"

def getvalues():
  return 12,23

noReturn()

retVal = oneRetValue()
print(retVal)

num1,num2 = getvalues()
print(num1)
print(num2)