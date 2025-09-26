list1 = ["how are you", "hey everyone", "are you there"]
word_counts = {}

for phrase in list1:
    words = phrase.split()
    for word in words:
        word = word.lower()

        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1


for word, count in word_counts.items():
    print(f"{word}:{count}")