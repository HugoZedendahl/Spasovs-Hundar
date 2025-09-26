


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
        temp = friends.get(name)
        donation += temp[1]
        friends.update({name:[1,donation]}) 
    else:
        print("Fel, inte inbjuden!")
    name = input("Namn: ")

#print(friends)

for namn, värde in friends.items():
    temp = friends.get(namn)
    if temp[0] == 1:
        print(f"{namn} : {värde[1]}")