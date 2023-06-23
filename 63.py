def displayshoes(item):
    for L in range(len(item)):
        print("รองเท้าหนังคู่ที่ ",L+4," = ",item[L])

def displayVet(item):
    for L in range(len(item)):
        print("รองเท้าแตะแบบที่ ",L+5," = ",item[L])

shoes=["boots","vintage shoes"]
vet=('green slippers','white slippers')

displayshoes(vet)