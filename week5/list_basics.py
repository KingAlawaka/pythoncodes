# https://www.w3schools.com/python/python_lists.asp

list1 = [1,2,3,4]
print(list1)
print(list1[2])

list2 = ["value1", 2, 3.4, True]
print(list2)
print(list2[1])

print("\nusing index and loop")
last_index = len(list1)-1
for i in range(0,len(list1)):
  print(f"index: {i} , value: {list1[i]}")

print("\nusing each item loop")
for i in list1:
  print(i)

print("\nusing enumerated")
for i, val in enumerate(list1):
  print(f"Index: {i} , value: {val} ")

"""
"""