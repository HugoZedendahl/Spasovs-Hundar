gather = True
mode = None
printStatement = ""
inventory = {
    "körv": 200,
    "brö": 400,
    "elva": 1,
    "höppa": 1,
    }

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
            
        
            
