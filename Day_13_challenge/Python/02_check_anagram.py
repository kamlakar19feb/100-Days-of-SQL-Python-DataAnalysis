Check if two strings are anagrams.
👉 Input: “listen”, “silent” → Output: True

str1=input("Enter first string: ")
str2=input("Enter second string: ")
sorted1=sorted(str1)
sorted2=sorted(str2)
if sorted1==sorted2:
  print("The strings are Anagrams")
else:
  print("Not anagrams")
