pares = 0
impares = 0
for c in range (0,11):
    numero = int(input("Digite um número: "))
    if numero %2 == 0:
        pares += 1
    else:
        impares += 1
print (f"{pares} números digitados eram pares")
print (f"{impares} números digitados eram ímpares")