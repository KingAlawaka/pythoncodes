import pythonModule as pyMod

val = pyMod.readIntInput("Please input value")
float_val = float(val)
print(float_val)

name = "simon hall"
f = open(name+".txt", "w")
print("writethis", file=f)

from random import randrange
print(randrange(1,6))
