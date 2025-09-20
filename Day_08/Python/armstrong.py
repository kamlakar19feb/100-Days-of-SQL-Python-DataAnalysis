Check if a number is Armstrong
👉 An Armstrong number is a number that is equal to the sum of its digits raised to the power of the number of digits.
Example: 153 = 1³ + 5³ + 3³

n= int(input("Enter number: "))
len_n=len(str(n))
temp=n
sum_val=0
while temp>0:
  digit=temp%10
  sum_val=sum_val+pow(digit,len_n)
  temp=temp//10
if n==sum_val:
  print("The given number n is an Armstrong number")
else:
  print("Not an Armstrong number")
