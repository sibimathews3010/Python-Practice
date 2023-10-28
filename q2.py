def max_min(arr):
  arr.sort()
  max_sum=sum(arr[1:])
  min_sum=sum(arr[:-1])
  print(max_sum, min_sum)
arr = list(map(int,input().rstrip().split(",")))
max_min(arr)
