def test():
  print("inside the function")

val = test()
print(val)
#print(val == "None")
print(type(val))

def func(a, b):
     num = a % b
     return num
print(func(3,7))