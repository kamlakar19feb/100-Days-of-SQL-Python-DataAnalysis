#1.	Reverse a string without using slicing ([::-1]).
Example: "hello" → "olleh"

string1=input("Enter string1: ")
rev = ""
for char in range(len(string1)-1,-1,-1):
  rev=rev+string1[char]
print("reverse string1: ", rev)

#2.	Find the second largest number in a list.
Input: [12, 45, 67, 23, 89, 45] → Output: 67
nums = list(map(int, input("Enter space separated numbers: ").split()))

largest = max(nums)
second_largest = float("-inf")

for i in nums:
    if i != largest and i > second_largest:
        second_largest = i

if second_largest == float("-inf"):
    print("No second largest (all numbers are the same)")
else:
    print("Second largest =", second_largest)
