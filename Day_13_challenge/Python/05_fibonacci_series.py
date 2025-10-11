Generate Fibonacci series up to n terms (using while loop).
👉 Input: 7 → Output: 0 1 1 2 3 5 8

n1=int(input("Enter number: "))
fibo_series=[0,1]
result=0
count=2
while count<n1:
  result=fibo_series[-1]+fibo_series[-2]
  fibo_series.append(result)
  count+=1
print(fibo_series)
