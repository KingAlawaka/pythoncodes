list1 = [1,2,3,4]
print(list1)

print(list1[0])
print(len(list1))
list2 = [5,6] + list1
print(list2)

for i in range(0,len(list1)):
  print(list1[i])

for i in list1:
  print(i)

countries = ["spain", "brazil", "portugal", "bolivia"]
print(countries)
countries.append("italy")
print(countries)
countries.reverse()
print(countries)

for i in range(0,len(countries)):
  if countries[i]=="spain":
    print("location ", str(i))
  print(countries[i])

print(min(list2))
print(max(list2))
print(list1.index(min(list1)))
list2.sort(reverse=True)
print(list2)
