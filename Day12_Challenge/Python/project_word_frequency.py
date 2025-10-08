Python Project:

Word Frequency Counter (Case-insensitive)
Input: a paragraph
Output: Top 3 most frequent words and their counts.

paragraph=input("Enter paragraph: ")
paragraph=paragraph.lower()
word_count={}
for word in paragraph.split():
  if word in word_count:
    word_count[word]+=1
  else:
    word_count[word]=1
sorted_dict=sorted(word_count.items(), key= lambda x:x[1], reverse=True)[:3]
print(sorted_dict)
