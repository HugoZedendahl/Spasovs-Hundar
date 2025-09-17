string = input("input sentecnce. ")
längst = ""
längstLängd = 0
currentWord = ""
currentLength = 0
totalWords = 0
firstWord = False

#this is a very inefificient way of doing this, but since we have not learned about slicing yet, this is functional enough
#it also does not account for special symbols like !"#¤%&/()=?:,. etc i think a regex would be ideal for this. 
#i however, do not know how to properly use them at all and they scare me.  //HZ

for x in string:
    if x != " ":
        firstWord = True
        currentLength +=1
        currentWord += x
        
    elif x == " " and firstWord == True:
        totalWords +=1
        if currentLength > längstLängd:
            längst = currentWord
        currentLength = 0
        currentWord = ""
            
    else:
        pass
    
totalWords +=1
if currentLength > längstLängd:
    längst = currentWord
currentLength = 0
currentWord = ""

print("det var", totalWords,'ord i strängen och "', längst,'" var det längsta ordet')  
