# Øvelse 10: Debugging Practice
tekst = input("Skriv tall med mellomrom (f.eks. 10 5 20): ")
biter = tekst.split()               # deler teksten på mellomrom -> liste
print("Etter split:", biter)        # debug: se hva vi faktisk fikk

tall = []
for bit in biter:
    try:
        tall.append(int(bit))       # prøv å gjøre om til tall
    except ValueError:              # hvis det ikke er et tall...
        print(f"'{bit}' er ikke et tall - hopper over")

print("Tall-lista:", tall)          # debug
print("Summen er:", sum(tall))


# Øvelse 4: Math Quiz with Exception Handling
import random

a = random.randint(1, 10)
b = random.randint(1, 10)

while True:
    svar = input(f"Hva er {a} + {b}? ")
    try:
        svar_tall = int(svar)        # gyldig tall? da hopper vi ut
        break
    except ValueError:
        print("Skriv et tall, er du snill!")

if svar_tall == a + b:
    print("Riktig!")
else:
    print(f"Feil - riktig svar var {a + b}")


    

# Øvelse 1: File to List Converter
filnavn = input("Hvilken fil vil du lese? ")
try:
    with open(filnavn, "r") as fil:     # åpne fila for lesing
        linjer = fil.readlines()        # les alle linjer inn i en liste
    reine = []
    for linje in linjer:
        reine.append(linje.strip())     # strip() fjerner mellomrom/linjeskift
    print(reine)
except FileNotFoundError:               # hvis fila ikke finnes
    print("Fant ikke den fila.")