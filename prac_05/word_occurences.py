"""
Word Occurrences
Estimate: 10 minutes
Actual:   20 minutes
"""

user_message = input("Text: ")

words = user_message.split()
words.sort()
word_to_count = {}

for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

for word, count in word_to_count.items():
    print(f"{word:12}: {count}")