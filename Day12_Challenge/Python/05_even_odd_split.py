From a given list [1,2,3,4,5,6,7,8,9], create two lists — one with even numbers and one with odd numbers.

nums = list(map(int, input("Enter numbers: ").split()))
even_list=[]
odd_list=[]
for i in nums:
  if i%2==0:
    even_list.append(i)
  else:
    odd_list.append(i)
print("List of even numbers: ", even_list)
print("List of odd numbers: ", odd_list)
