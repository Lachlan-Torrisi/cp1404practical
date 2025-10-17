"""
Word Occurrences
Estimate: 10 minutes
Actual:   
"""

user_message = input("Text: ")

words = user_message.split()
word_to_count = {}

for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

print(word_to_count)