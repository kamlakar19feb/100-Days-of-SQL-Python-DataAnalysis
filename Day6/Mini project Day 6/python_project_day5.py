#Python Project
#Task: Write a program that takes a list of numbers and removes all duplicates while keeping the order.
#Example: [1,2,2,3,4,4,5] → [1,2,3,4,5]

nums=list(map(int,input("Enter space separated numbers: ").split()))
unique_nums=[]
for i in nums:
  if i not in unique_nums:
    unique_nums.append(i)
print("Updated list= ", unique_nums)
