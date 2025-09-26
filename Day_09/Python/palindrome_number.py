number1=int(input("Enter number: "))
rev_num=0
temp=number1
while temp>0:
  t1=temp%10
  rev_num=rev_num*10+t1
  temp=temp//10
if rev_num==number1:
  print("Palindrome")
else:
  print("Not a Palindrom")
