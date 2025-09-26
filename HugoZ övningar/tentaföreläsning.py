
friends = {
    "peter": [0,0],
    "mia": [0,0],
    "henke": [0,0],
    "jozef": [0,0],
    "lena": [0,0],
    "stefan": [0,0],
    "perka": [0,0],
    "micke": [0,0],
    "sussi": [0,0]
}

name = input("Namn: ")
while name != "sluta":
    if name in friends:
        donation = input("Belopp: ")
        donation = int(donation)
        friends.update({name:[1,donation+friends.get(name)[1]]}) 
    else:
        print("Fel, inte inbjuden!")
    name = input("Namn: ")
    
for namn, värde in friends.items():
    if värde[0] == 1:
        print(f"{namn} : {värde[1]}")