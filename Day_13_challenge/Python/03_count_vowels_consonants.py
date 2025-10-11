Count vowels and consonants in a sentence.
👉 Input: “Data Analytics” → Output: Vowels = 5, Consonants = 8

import re
sen1=input("Enter sentence: ")
sen1=sen1.lower()
cleaned=re.sub(r'[^A-Za-z]','',sen1)
print(cleaned)
vowels='aeiou'
Vowels_count=0
Consonants_count=0
for ch in cleaned:
  if ch in vowels:
    Vowels_count+=1
  else:
    Consonants_count+=1
print("Vowels= ", Vowels_count)
print("Consonants= ", Consonants_count)
