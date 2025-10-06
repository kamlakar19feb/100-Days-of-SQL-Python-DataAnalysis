1️⃣ Find all perfect numbers up to n

A perfect number is equal to the sum of its positive divisors, excluding itself.

Example: 6 → divisors 1, 2, 3 → sum = 6

n=int(input("Enter number upto which perfect numbers to be listed: "))
list1=[]
for i in range(1,n+1):
  sum1=0
  for j in range(1,i):
    if i%j==0:
      sum1=sum1+j
  if sum1==i:
    list1.append(i)
print(list1)
