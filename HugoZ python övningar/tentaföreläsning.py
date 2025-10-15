
friends = {
    "peter": [False,0],
    "mia": [False,0],
    "henke": [False,0],
    "jozef": [False,0],
    "lena": [False,0],
    "stefan": [False,0],
    "perka": [False,0],
    "micke": [False,0],
    "sussi": [False,0]
}

name = input("Namn: ")
while name != "sluta":
    if name in friends:
        donation = input("Belopp: ")
        donation = int(donation)
        friends.update({name:[True,donation+friends.get(name)[1]]}) 
    else:
        print("Fel, inte inbjuden!")
    name = input("Namn: ")

for namn, värde in friends.items():
    if värde[0] == True:
        print(f"{namn} : {värde[1]}")