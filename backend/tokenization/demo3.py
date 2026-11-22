text = input("Enter a sentence: ") or "I love learning Python"

words = text.split()

print("Original Text:", text)
print("Total Words:", len(words))

print("Word by Word:")

for word in words:
    print(word)