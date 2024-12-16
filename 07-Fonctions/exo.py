#1)

def somme_liste(entiers: list[int]) -> int:
    
    s = 0
    for e in entiers:
        s += e

    return s

lst = [10,15,2,5,8]

r = somme_liste(lst)
print(r)

#2)
def moyenne_liste(entiers: list[int]) -> float:
    s = somme_liste(entiers)
    nb = len(entiers)
    return s / nb

print(moyenne_liste([1,2]))

#3)
def table_multiplication(nombre, premier_multiple, dernier_multiple):
    for i in range(premier_multiple, dernier_multiple + 1):
        print(f'{nombre} x {i} = {nombre * i}')



table_multiplication(11,1,12)
