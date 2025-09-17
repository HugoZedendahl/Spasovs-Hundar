gather = True
mode = None
printStatement = ""
inventory = {}

# you can also use 2 lists and and store the items and their amounts in the same index position. burt for this specific case
# a dictionary is better (in my personal opinion) //HZ
#while gather:
#    mode = str.lower(input("what item(s) do you want to query? :"))
#    match mode:
#        case "körv":
#            if str(inventory["körv"])+" "+str(mode)+"ar" not in printStatement:
#                printStatement += str(inventory["körv"])+" "+str(mode)+"ar"+","
#        case "brö":
#            if str(inventory["brö"])+" "+str(mode)+"n" not in printStatement:
#                printStatement += str(inventory["brö"])+" "+str(mode)+"n"+","
#        case "elva":
#            if str(inventory["elva"])+" "+str(mode) not in printStatement:
#                printStatement += str(inventory["elva"])+" "+str(mode)+","
#        case "höppa":
#            gather = False
#        case _:
#            print("vi har int detta")
#

try:
    inputArtickel = str(input("skriv in artickel: "))
    inputArtickelLager = 0
except: 
    print("skriv en sträng! jag vet faktiskt inte hur du skrev in annan data")
    quit()
#double loop to use "break" to restart the loop if a user fed a string value when a integer is needed.
while inputArtickel != "sluta":
    while inputArtickel != "sluta":
        try: 
            inputArtickelLager = int(input("skriv antal i lager: "))
            if inputArtickelLager not in inventory:
                inventory.update({inputArtickel:inputArtickelLager})
            elif inputArtickelLager in inventory:
                inventory[inputArtickel] = inputArtickelLager
            inputArtickel = str(input("skriv in artickel: "))   
        except:
            print("snälla skriv en siffra")
            break
    

print("vi har:")
for key, value in inventory.items() :
    print ("[",key,"]","[", value,"]")
   
            
        
            
