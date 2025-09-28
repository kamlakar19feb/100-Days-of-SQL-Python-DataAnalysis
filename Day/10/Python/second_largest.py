Find the second largest number in a list.
👉 Example: [10, 20, 4, 45, 99] → 45

nums=list(map(int,input("Enter space separated numbers: ").split()))
largest=max(nums)
second_largest=float('-inf')
for i in nums:
  if i != largest and i>second_largest:
    second_largest=i
if second_largest==float('-inf'):
  print("No second largest, all numbers are same")
else:
  print("Second largest = ", second_largest)
