Python Mini Project – Number Analyzer

Input: List of numbers

Output: List of prime numbers, list of Armstrong numbers, sum of all numbers

list_n=list(map(int,input("Enter space separated numbers: ").split()))
prime_list=[]
armstrong_list=[]
sum_list_n=0
#prime
for i in list_n:
  for j in range(2,int((i**0.5)+1)):
    if i%j==0:
      break
  else:
    prime_list.append(i)
print("list of prime numbers :", prime_list)
#armstrong
for i in list_n:
  digit = len(str(i))
  temp=i
  temp1=0
  result=0
  while temp>0:
    temp1=temp%10
    result+=temp1**digit
    temp=temp//10
  if result==i:
    armstrong_list.append(i)
print("list of armstrong numbers : ", armstrong_list)
#sum
for i in list_n:
  sum_list_n+=i
print("sum of all numbers from list: ", sum_list_n)
