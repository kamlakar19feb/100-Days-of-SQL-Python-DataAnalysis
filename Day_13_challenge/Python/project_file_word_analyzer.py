Python Mini Project: File Word Analyzer

Input: A text file (sample.txt)

Tasks:

Count total words

import re
with open("Sample_text.txt", "r") as file:
    content = file.read()
    words=content.split()
    total_words=len(words)
print("Total words in file:", total_words)



Find most frequent word

from collections import Counter
import re
with open("Sample_text.txt", "r") as file:
    content = file.read()
content_clean = re.sub(r'[^a-zA-Z0-9 ]', '', content)
words = content_clean.split()
words_count=Counter(words)
most_common_word,frequency= words_count.most_common(1)[0]
print("Most frequently used word:", most_common_word)
print("Frequency:", frequency)



Count lines in the file

count=0
with open("Sample_text.txt", "r") as file:
  for line in file:
    count += 1
print("Total number of lines:", count)
