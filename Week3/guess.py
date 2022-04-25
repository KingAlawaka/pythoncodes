name = "RUWANDA"
for a in range(len(name)):
  if a == 1 or a == 3 or a == 5:
    print("_", end=" ")
  else:
    print(name[a], end=" ")
print()
guess_val = input("enter your name")
print(name == guess_val)