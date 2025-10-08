Calculate the sum of digits of a number until a single digit remains (e.g., 9875 → 2).

n=int(input("Enter number: "))
result=n
while result>9:
  temp_sum=0
  while result>0:
    temp_sum+=result%10
    result=result//10
  result=temp_sum
print("Single digit sum:", result)
