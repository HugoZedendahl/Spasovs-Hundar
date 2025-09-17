mening = input("Ange din mening: ")
meningSomLista = mening.split()
antalOrd = len(meningSomLista)

storlek = 0     #skapar ny variabel för att kunna jämföra indexobjekt
störstaOrd = []     #skapar en lista där alla de största orden sparas
for x in meningSomLista:    #loop som går igenom varje instans av listan "meningSomLista"
    if len(x) > storlek and len(x) != storlek:    #loop som kollar om längden på varje index är större än variabeln "storlek"
        storlek = len(x)     #variabeln "storlek" uppdateras med längden på det hitills längsta ordet
        störstaOrd = []     #listan nollställs så att det enda som sparas är det största värdet hittills 
        störstaOrd.append(x)    #största värdet sparas i en ny lista -> "störstOrd"
    elif len(x) == storlek:     #loop som kollar om (x) är lika stort som "storlek"
        störstaOrd.append(x)    #om storleken på (x) är lika stor sparas det också i listan "storaOrd"

summaBokstäver = []     #skapar en lista för att spara alla siffror (längden på orden)
for x in störstaOrd:     #loop som går igenom listan "störstOrd"
    summaBokstäver.append(len(x))      #lägger till varje längd i listan "summaBokstäver"

summaBokstäver.sort(reverse=True)   #sorterar listan "summaBokstäver" i nummerär ordning med det högsta först. summaBokstäver[0] = största ordet
for x in störstaOrd:    #loop som går igenom lsitan "störstOrd"
    if len(x) < summaBokstäver[0]: #loop som jämför längden på alla objekt i listan "summaBokstäver" med storleken på största ordet
        störstaOrd.remove(x)    #om storleken är mindre än storleken på största ordet tas de bort ur listan

print("Antal ord är", antalOrd)
print("Längst ord är:")
for x in störstaOrd:
    print(x)

