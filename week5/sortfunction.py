def myFunc(e):
  if (e[0] == "F"):
    return "a"
  elif (e[0] == "V"):
    return "0"
  else:
    return "2"

def myFunc2(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc2)

print(cars)
