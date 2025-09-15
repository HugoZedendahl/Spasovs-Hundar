string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam molestie, libero quis rhoncus luctus, risus est feugiat sem, eget rutrum risus ipsum nec ipsum. Proin purus sapien, euismod sit amet commodo ac, ornare ac diam. Ut venenatis, erat sit amet dictum vulputate, nisl turpis consectetur eros, a iaculis tortor purus ut magna. Vivamus tincidunt aliquam egestas. In fermentum vestibulum diam, id bibendum metus fringilla vel. Curabitur sed libero commodo, commodo arcu quis, blandit mi. Aliquam erat volutpat. Nunc posuere, orci eget venenatis tincidunt, tortor tortor iaculis ex, eget fringilla urna felis a elit. Proin eu egestas mauris. Donec vehicula interdum neque, vel porta odio mollis nec. Vestibulum posuere venenatis iaculis. Cras vitae augue et sapien dapibus facilisis ac eget lectus. Maecenas sem felis, pulvinar sit amet mi ut, suscipit pulvinar velit. Nunc nisi elit, porttitor quis vehicula imperdiet, pellentesque ut urna. Aliquam sed nisi nec sapien rutrum gravida. Integer eget est felis."

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
