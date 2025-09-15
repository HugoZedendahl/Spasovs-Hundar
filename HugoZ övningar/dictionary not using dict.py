swedishStringList = ["hund", "katt", "ödla", "häst", "ko", "kanin"]
englishStringList = ["dog", "cat", "lizzard", "horse", "cow", "rabbit"]

indexValue = input("skriv ditt ord: ")
indexValue = indexValue.lower()
if indexValue in swedishStringList:
    print("ditt ord på engelska är: ", englishStringList[swedishStringList.index(indexValue)])

elif indexValue in englishStringList:
    print("ditt ord på svenska är: ", swedishStringList[englishStringList.index(indexValue)])

else:
    print("ditt ord finns inte i vår ordbok")
