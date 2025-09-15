gather = True
mode = None
printStatement = ""
inventory = {
    "körv": 200,
    "brö": 400,
    "elva": 1,
    "höppa": 1,
    }
# you can also use 2 lists and and store the items and their amounts in the same index position. burt for this specific case
# a dictionary is better (in my personal opinion) //HZ
while gather:
    mode = str.lower(input("what item(s) do you want to query? :"))
    match mode:
        case "körv":
            if str(inventory["körv"])+" "+str(mode)+"ar" not in printStatement:
                printStatement += str(inventory["körv"])+" "+str(mode)+"ar"+","
        case "brö":
            if str(inventory["brö"])+" "+str(mode)+"n" not in printStatement:
                printStatement += str(inventory["brö"])+" "+str(mode)+"n"+","
        case "elva":
            if str(inventory["elva"])+" "+str(mode) not in printStatement:
                printStatement += str(inventory["elva"])+" "+str(mode)+","
        case "höppa":
            gather = False
        case _:
            print("vi har int detta")

print("vi ha:",printStatement)
            
        
            
