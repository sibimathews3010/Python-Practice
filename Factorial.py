#factorial
def fact(n):
  r=1
  for i in range(1,n+1):
      r=r*i
  return r
n = int(input("Enter a number: "))
print("factoril=",fact(n))
