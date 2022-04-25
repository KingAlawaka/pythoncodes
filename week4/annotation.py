def foo(a:"int", b:"float"=5.0)  -> "int":
  number = a * b
  return number

n = foo("23",3.0)
print(n)
print(type(n))
print(foo.__annotations__)


