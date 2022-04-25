def changeVal1(number):
  number = number *  2
  print("inside the function ", number)
  return number

def main():
  val = 5
  print("before change ", val)
  changeVal1(val)
  print("after change ", val)
  #val = changeVal1(val) #10
  #print("return use ", val)
  #val = changeVal1(val)
  #print("Now value ", val)

main()