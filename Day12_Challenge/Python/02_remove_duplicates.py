Given a list of numbers, remove duplicates without using set().

nums = list(map(int, input("Enter numbers: ").split()))
list_uniq=[]
for i in nums:
  if i not in list_uniq:
    list_uniq.append(i)
print(list_uniq)
