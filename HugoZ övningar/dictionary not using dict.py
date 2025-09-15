swedishStringList = ["hund", "katt", "ödla", "häst", "ko", "kanin"]
englishStringList = ["dog", "cat", "lizzard", "horse", "cow", "rabbit"]
indexValue = None

while indexValue != " ":
    indexValue = input("skriv ditt ord: ")
    indexValue = indexValue.lower()
    if indexValue in swedishStringList:
        print("ditt ord på engelska är: ", englishStringList[swedishStringList.index(indexValue)])

    elif indexValue in englishStringList:
        print("ditt ord på svenska är: ", swedishStringList[englishStringList.index(indexValue)])

    else:
        print("ditt ord finns inte i vår ordbok")

#simple and effective. find the index of the input and use that to print the corresponding word from the other language. //HZ 