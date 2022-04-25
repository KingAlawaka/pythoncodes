def displayFirstandLastLetter(list):
  for a in list:
    print(a[0],a[len(a)-1])

def avgLengthofEmails(emails):
  totalLength = 0
  for a in emails:
    totalLength = totalLength + len(a)
  return totalLength/len(emails)
  

def main():
  names = ["jack","john","mike"]
  emails = ["jack@gmail.com","john@gmail.com","mike@gmail.com"]
  displayFirstandLastLetter(names)
  print(avgLengthofEmails(emails))


main()