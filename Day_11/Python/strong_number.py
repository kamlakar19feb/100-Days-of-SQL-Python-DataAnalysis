2️⃣ Check if a number is a strong number

A strong number is a number equal to the sum of factorials of its digits.

Example: 145 → 1! + 4! + 5! = 145

n=int(input("Enter number upto which strong numbers to be listed: "))
list2=[]
fact=[1]
for k in range(1,10):
  fact_k=fact[k-1]*k
  fact.append(fact_k)
for j in range(1,n+1):
  temp_j=j
  sum2=0
  temp=0
  while temp_j>0:
    temp=temp_j%10
    sum2=sum2+fact[temp]
    temp_j=temp_j//10
  if sum2==j:
    list2.append(j)
print(list2)
