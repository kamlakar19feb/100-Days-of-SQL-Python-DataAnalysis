import re 
string1=input("Enter string: ") 
cleaned= re.sub(r'[^A-Za-z]','',string1)
print("cleaned string=", cleaned)
dict1={}
for i in cleaned:
  if i in dict1:
    dict1[i]+=1
  else:
    dict1[i]=1
print("the freq of each word is:", dict1)
