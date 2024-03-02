'''
projekt_1.py: první projekt do Engeto online Python Akademie

author = Jana Wolfová

email: janarega@seznam.cz

discord: jana_73904
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
#registrované osoby
registr = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

#přihlašovací martirium
user = input("username: ")
if user in registr:
    while True:
        password = input("password: ")
        if registr[user] == password:
            print("-" * 40)
            print("Welcome to the app, ", user, "\nWe have 3 texts to be analyzed." )
            print("-" * 40)
            break
        else:
            print("Špatné heslo, zkuz to znova")
else:
    print("unregistered user, terminating the program.. ")
    exit()

#výběr textu 1 až 3 nebo vyhazov

vybery = [1, 2, 3]

vyber = input("Enter a number btw. 1 and 3 to select: ")
print("-" * 40)
if not vyber.isdigit():
    print("Nesprávný vstup, ukončuji program!!")
    exit()

vyber = int(vyber)

if vyber not in vybery:
    print("Nesprávný vstup, ukončuji program!!")
    exit()
else:
    x = vyber - 1

#vybere text ze seznamu
txt = TEXTS[x]

#očistí text od interpunkce atd
ctxt = txt.replace(".", " ").replace(",", " ").replace("-", " ").replace("'", " ")
#rozkouskuje 
slova = ctxt.split()



#počet slov
pocet_slov = len(slova)
print("There are ", pocet_slov, "words in the selected text.") 

#počet slov začínající velkým písmenem
pocet_velkych_pismen = 0
for slovo in slova:
    if slovo.istitle():
        pocet_velkych_pismen += 1
print("There are ",pocet_velkych_pismen, "titlecase words.")

#počet slov psaných velkými písmeny
velke = 0
for slovo in slova:
    if slovo.isupper():
        velke += 1
print("There are ", velke, "uppercase words.")

#počet slov psaných malými písmeny
male = 0
for slovo in slova:
    if slovo.lower():
        male += 1
print("There are ",male, "lowercasse words.")

#počet čísel a jejich součet 
cislo = 0
soucet = 0
for slovo in slova:
    if slovo.isdigit():
        cislo += 1
        soucet += int(slovo)
print("There are ", cislo, "numeric strings.")
print("The sum of all the numbers ",soucet)

print("-" * 40)
print("LEN|   OCCURENCES           | NR.")
print("-" * 40)


pocet_delek = {}
pocet = 0


#procházení textu
for slovo in slova:
    if slovo.isalnum():
        delka = len(slovo)

    # Pokud délka slova není ve slovníku,vytvoří, jinak přičte k existující
    if delka not in pocet_delek:
        pocet_delek[delka] = 1
    else:
        pocet_delek[delka] += 1


 # pro délku a počet stejně dlouhých slov seřadit a vypsat 
for delka, pocet in sorted(pocet_delek.items()):
    if delka < 10:
        print( delka, " |", (pocet * "*") + (21 - pocet) * " ", " |", pocet)
    else:
        print( delka, "|", (pocet * "*") + (22 - pocet) * " ", "|", pocet)
