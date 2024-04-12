lista = [2,4,7,2,3,3,1,0,2,6]
teste = len(lista)
maximo = max(lista)
comparador = 0
for c in range (0,maximo):
    num = lista.count(c)
    if num > comparador:
        comparador = c
print (comparador)
    