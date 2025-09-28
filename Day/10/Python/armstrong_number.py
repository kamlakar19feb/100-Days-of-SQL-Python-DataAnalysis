Check if a number is Armstrong (without using strings).
👉 Example: 153 → Armstrong (1³ + 5³ + 3³ = 153)


n=int(input("Enter number: "))
temp=n
sum1=0
digits = len(str(n))
while n>0:
  i=n%10
  sum1=sum1+pow(i,digits)
  n=n//10
if temp==sum1:
  print("number is Armstrong")
else:
  print("Number is not Armstrong")
