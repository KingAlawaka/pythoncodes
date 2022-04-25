from paint import Paint

def main():
  p1 = Paint("CIC","Red",123,2)
  p2 = Paint("ACB","Black",250,4)

  print(p1)
  print(p2)

  p1Cost = p1.getCost()
  p2Cost = p2.getCost()
  print(p1Cost)
  print(p2Cost)

main()