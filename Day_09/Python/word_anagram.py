word=input("Enter word: ")
print(word)
words = input("Enter list of words separated by space: ").split()
print(words)
anagrams =[]
sorted_word=sorted(word)
for w in words:
  if sorted(w)==sorted_word:
    anagrams.append(w)
print("anagrams:", anagrams)
