def largest_(list1):
  return max(list1)
# take input from user
user_input=input("Enter list of numbers separated by spaces: ")
numbers=list(map(int,user_input.split()))
print("largest number = ", largest_(numbers))
