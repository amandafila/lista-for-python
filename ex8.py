cont = 0
numero = int(input("Digite um número: "))
for c in range (1, numero):
    if numero % c == 0:
        print(c)