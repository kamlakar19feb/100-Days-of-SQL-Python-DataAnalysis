Count vowels and consonants in a string
👉 Input: "Hello World" → Output: Vowels = 3, Consonants = 7

import re
string1=input("Enter string: ")
cleaned= re.sub(r'[^A-Za-z]','',string1)
vowels='aeiou'
c_vowels=0
c_cons=0
for char in cleaned:
  if char in vowels:
    c_vowels+=1
  else:
    c_cons+=1
print("Vowels= ", c_vowels)
print("Consonants= ", c_cons)
