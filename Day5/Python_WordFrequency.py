from collections import Counter
sent1 = input("Enter sentence: ")
word_freq = Counter(sent1.split())
print(word_freq)
