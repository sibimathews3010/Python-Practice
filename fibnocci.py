from re import L
#Generate a Fibonacci Series:using array and function
def fibonacci(n):
    series = [0, 1]
    for i in range(2,n):
        series.append(series[-1]+series[-2])
    return series
num_terms = int(input("Enter the number of terms in the Fibonacci series: "))
result = fibonacci(num_terms)
print("Fibonacci Series:", result)
#Simple

print("Fibonacci Series:\n0\n1")
k=0
l=1
m=k+l
for i in range(2,num_terms):
  print(m)
  k=l
  l=m
  m=k+l









