#Skriv ett Python-program som från användaren läser en lång textrad bestående av flera ord
#avdelade med mellanslag. Med ord här menas bara följder av icke-blanka tecken avdelade
#med mellanslag, det behöver inte vara existerande ord i något språk. Programmet ska skriva ut
#hur många ord som finns i texten och vilket som är det längsta ordet.
#Om det finns flera ord som är lika långa som längsta ordet så kan du själv välja vad som ska
#skrivas ut – alternativen är det först påträffade ordet med störst längd, det sist påträffade ordet
#med störst längd eller (helst men svårast) alla ord med den längden.


mening = input("Skriv ett antal ord! ")
while mening != "sluta":
    preant = mening.split()
    antal = len(preant)
    långt = ""

    for x in preant:
        if len(x) > len(långt):         # len(x)är längden på de enskilda elementen
            långt = x

    print("Du skrev", antal, "ord!")
    print("Det längsta ordet du skrev var:",långt)
    
    mening = input("Skriv ett antal ord! ")

