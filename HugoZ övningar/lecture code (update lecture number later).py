def pause (message, rows, char):
    for r in range(0, rows):
        print(char*50)
    input(message)

print("javisst gör det ont när knoppar brister")
pause("tryck på RETURN för andra raden",2,"-")
print("varför skulle annars våren tveka")
pause("tryck på RETURN för att avsluta",4,"+")

pause("Hej", 4, "+")

pause(char="-", rows=2, message="hej")
#this thing non positional call  is uniqe to python

# def pause (message, rows=3, char='-'):
#    for r in range(0, rows):
#        print(char*50)
#    input(message)
#   example of default values in functions. 
#   these arguments need to be the last declared
#   

def power (base, exp):
    if exp < 0:
        return 0
    result = 1
    for x in range(exp):
        result = result * base
    return result
x = None
y = None   
x = power(2,3)
y = 13* power(3,x)



