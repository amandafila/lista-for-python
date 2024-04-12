cont = 0
fora = 0
for c in range (0, 10):
    num = int(input("Digite um número: "))
    if num < 20 and num > 10:
        cont += 1
    else: 
        fora += 1
print (f"{cont} números estão dentro do intervalo")
print (f"{fora} números estão fora do intervalo")