text = open("igelkott.txt", "r")
allLines = text.readlines()
text.close()
tracker = {}
wordList = []
countList = []

for line in allLines:
    line = line.lower
    line = line.split()
    for word in line:
        if word not in tracker:
            tracker.update({word:0})
        elif word in tracker:
            tracker[word] += 1
for line in allLines:
    line = line.lower
    line = line.split()
    for word in line:
        if word not in wordList:
            wordList.append(word)
            countList.append(1)
        if word in wordList:
            countList[wordList.index(word)] += 1

    

print("orden i texten är följande")
for word, amount in tracker.items:
    print(f"[{word}]    [{amount}]")

print("orden i texten är följande")
for word in wordList:
    print(f"({word})    ({countList[wordList.index(word)]})")


print()