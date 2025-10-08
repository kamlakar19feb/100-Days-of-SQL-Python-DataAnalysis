Write a function that takes a sentence and returns the word with the maximum length.

def longest_word():
  sentence=input("Enter sentence: ")
  max_length=0
  longest_word1=''
  for word in sentence.split():
    if len(word)>max_length:
      max_length=len(word)
      longest_word1=word
  print("Longest_word is : ", longest_word1)
longest_word()
