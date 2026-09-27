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