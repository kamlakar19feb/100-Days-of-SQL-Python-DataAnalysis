 Reverse each word in a sentence (keep word order same).
👉 Input: “Python is fun” → Output: “nohtyP si nuf”

sen1=input("Enter sentence: ")
list1=[]
for word in sen1.split():
  word = ''.join(reversed(word))
  list1.append(word)
sen1=' '.join(list1)
print(sen1)
