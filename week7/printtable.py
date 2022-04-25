WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') 
print("{: <15} {: <10}".format("Day", "Calaries"))
for i in range(7):
    print("{: <15} {: <10}".format(WEEK[i], i*23))