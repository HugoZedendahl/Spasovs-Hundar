wordList = open("svenskaOrd.txt","r").readlines()
wordInput = input("välj ordet vi ska rimma: ")

while wordInput !=  "":
    for word in wordList:
        x = word.strip()
        x.lower()
        processedWord = wordInput.strip()
        processedWord.lower()
        if x[-2:-1] == processedWord[-2:-1]:
            print(x)
    wordInput = input("välj ordet vi ska rimma: ")