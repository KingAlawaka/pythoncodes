#https://www.geeksforgeeks.org/is-python-call-by-reference-or-call-by-value/
number =0 
list =[]
def changeValue(n):
  n = n + 1

print(f"Before change value {number}")
changeValue(number)
print(f"After change value {number}")

listValues = [10,23,45,21]

def changeList(l):
  for item in l:
    item = item/2

print(f"Before change list {listValues}")
changeList(listValues)
print(f"After change value {listValues}")

def changeList2(l):
  n = []
  for i in range(len(l)):
    n.append(l[i]/2)
  return n

print(f"Before change list {listValues}")
nn = changeList2(listValues)
print(f"After change value {listValues}")