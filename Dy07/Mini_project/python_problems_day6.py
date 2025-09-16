Task: Create a simple word frequency analyzer that ignores punctuation and counts the most frequent word.
Input: "Hello hello, world! World world." → Output: world → 3.

sent1=input("Enter sentence: ") 
cleaned=re.sub(r'[^a-zA-Z0-9]',' ',sent1).lower()
words=cleaned.split()
word_freq={} 
for w in words: 
  if w in word_freq: 
    word_freq[w] += 1 
  else: 
    word_freq[w]=1
max_word=max(word_freq,key=word_freq.get)
print("Max word Frequency:", max_word, "=>", word_freq[max_word])
