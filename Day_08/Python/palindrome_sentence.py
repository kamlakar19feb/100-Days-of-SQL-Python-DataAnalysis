Palindrome Checker for Sentences

Ignore spaces, punctuation, and case.
👉 Input: "A man, a plan, a canal: Panama" → Output: ✅ Palindrome

string1=input("Enter String: ")
cleaned=re.sub(r'[^a-z]',"", string1.lower())
lst1=list(cleaned)
if lst1[::]==lst1[::-1]:
  print("Palindrom")
else:
  print("Not a Palindrom")
