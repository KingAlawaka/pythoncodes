def testFunction(num):
  if num >= 0 and num%7 == 0:
    return True
  else:
    return False

def uppercaseAndLowercase(val):
  uppercaseCount = 0
  lowercaseCount = 0
  for letter in val:
    if letter.isupper():
      uppercaseCount = uppercaseCount+1
    else:
      lowercaseCount = lowercaseCount+1
  return uppercaseCount,lowercaseCount

def main():
  print(testFunction(7))
  print(testFunction(-2))
  print(testFunction(24))

  uppercase,lowercase = uppercaseAndLowercase("School")
  print(uppercase)
  print(lowercase)

main()
  
    
    