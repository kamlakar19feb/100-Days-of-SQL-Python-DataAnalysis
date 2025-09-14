1.	Reverse a string without using slicing ([::-1]).
Example: "hello" → "olleh"

string1=input("Enter string1: ")
rev = ""
for char in range(len(string1)-1,-1,-1):
  rev=rev+string1[char]
print("reverse string1: ", rev)
